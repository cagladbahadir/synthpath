from importer import *
from clip.simple_tokenizer import SimpleTokenizer as _Tokenizer
from model_and_processor_load import model_select
from mistral_reader import mistral_test_prompt_read
from model_and_processor_load import tokenizer_select, tokenize_custom
from evaluation import zeroshot_classification
from inference_dataset_representation_generate import inference_on_dataset
_Tokenizer = _Tokenizer()

def parser_func():
    ## Training time
    parser = argparse.ArgumentParser()
    parser.add_argument("--fixed_embedding", default = 'synth_net')
    parser.add_argument("--subtype", default='B-32')
    parser.add_argument("--dataset", default = 'MHIST')
    parser.add_argument("--length", default='long')
    parser.add_argument("--lora_layers", default='all')
    parser.add_argument("--lora_rank", default=8)
    parser.add_argument("--lora_alpha", default = 8)
    parser.add_argument("--lora_bias", default="none")
    parser.add_argument("--lora_dropout", default=0.05)
    parser.add_argument("--context_lambda", default = 0.5)
    parser.add_argument("--context_type", default = '')
    parser.add_argument("--rewrite_count", default=5)
    return parser

parser = parser_func()
args = parser.parse_args()

fixed_embedding = args.fixed_embedding
subtype = args.subtype
subtype = subtype.replace("/", "_")
context_text = '_context' if float(args.context_lambda) > 0 else ''
folder_path =   os.path.abspath(os.path.join(os.path.dirname(__file__), '..', ''))
savepath = (folder_path + '/Test_Results/Zero_Shot_Classification/'+args.dataset+"/"+args.fixed_embedding + context_text +'/'+subtype+'/')
if not os.path.isdir(savepath): os.makedirs(savepath)
device = "cuda:0" if torch.cuda.is_available() else "cpu"  # If using GPU then use mixed precision training.

# Context and embedding models
frozen_model, preprocess_frozen_model = model_select('frozen', fixed_embedding, device, args.subtype, args)
embedding_model = TextCLIP(frozen_model, args.fixed_embedding).to(device)

tokenizer = tokenizer_select(fixed_embedding, preprocess_frozen_model)

inference_on_dataset(args)

test_features = torch.load(folder_path + '/Embeddings/'+args.dataset+'/'+fixed_embedding+"/"+subtype+'/test_image_features.pt', map_location = 'cpu')
lbl = torch.load(folder_path +'/Embeddings/'+args.dataset+'/'+fixed_embedding+  "/"+subtype+'/labels.pt', map_location = 'cpu')
with open(folder_path + '/Embeddings/'+args.dataset+'/'+fixed_embedding+ "/"+subtype+'/label_dict.pickle', 'rb') as handle:
    label_dict = pickle.load(handle)


gpt_prompts = mistral_test_prompt_read(args.dataset)
context_model =  torch.nn.Embedding(3, 512)

weight_path_context = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'weights/'))
checkpoint = torch.load(weight_path_context + '/synth_path_context_checkpoint.pt', map_location = device)
pretrained_dict = checkpoint['model_state_dict']
context_model.load_state_dict(pretrained_dict, strict=True)
context_model = context_model.to(device)


with torch.no_grad():
    if args.context_type == '':
        if (args.dataset in ['Pannuke_Organ','Ocelot_Organ'] ) and args.fixed_embedding == 'synth_net' and float(args.context_lambda) > 0:
            context = torch.tensor(1).to(device)
            context_embedding = context_model(context)
        elif (args.dataset in ['Pannuke_Cell','Ocelot_Cell',  'Skin_cancer', 'Renal_cell', 'CRC', 'SICAP'] ) and args.fixed_embedding == 'synth_net' and float(args.context_lambda) > 0:
            context = torch.tensor(0).to(device)
            context_embedding = context_model(context)
        elif (args.dataset in ['BACH', 'LC_Colon', 'LC_Lung', 'Skin_tumor', 'Camelyon', 'Databiox','MHIST'] ) and args.fixed_embedding == 'synth_net' and float(args.context_lambda) > 0:
            context = torch.tensor(2).to(device)
            context_embedding = context_model(context)
    else:
        if args.context_type == 'cell':
            context = torch.tensor(0).to(device)
            context_embedding = context_model(context)
        elif args.context_type == 'organ':
            context = torch.tensor(1).to(device)
            context_embedding = context_model(context)
        elif args.context_type == 'disease':
            context = torch.tensor(2).to(device)
            context_embedding = context_model(context)

for i in range(len(test_features)):
    if float(args.context_lambda) > 0 and args.fixed_embedding == 'synth_net':
        test_and_context = test_features[i]  * context_embedding.cpu()
        test_features[i] = test_and_context / test_and_context.norm(dim=-1, keepdim=True)
    else:
        test_features[i] = test_features[i] / test_features[i].norm(dim=-1, keepdim=True)

test_features = test_features.float()

result_dict = {}

print('Image embedding loaded.')
caption_dict = {}
text_embedding = []
for i in range(len(label_dict.keys())):
    print(i)
    caption = label_dict[i]
    tokenized = tokenize_custom(caption, tokenizer, fixed_embedding)
    embedding = embedding_model(tokenized.to(device))
    embedding_norm = embedding / embedding.norm(dim=-1, keepdim=True)
    caption_dict[i] = embedding_norm
    text_embedding.append(embedding_norm)
text_embedding = torch.vstack(text_embedding)
text_embedding = text_embedding.float().detach()

print('Text embedding acquired.')

if fixed_embedding != 'clip' :
    test_features = test_features.to(device).float()
    scale = frozen_model.logit_scale.exp().to(device).float()
else:
    test_features = test_features.to(device).half()
    scale = frozen_model.logit_scale.exp().to(device).half()

validation_accuracy, prompt_prob,  embedding_with_keys, logits = zeroshot_classification(image_features = test_features,
                                              class_labels = lbl.to(device),
                                              prompts = label_dict,
                                              embedding_model = embedding_model.to(device),
                                              model_logit = scale,
                                              preprocess = preprocess_frozen_model,
                                              model_name = fixed_embedding,
                                              device = device)

embedding_dict = {}
from collections import defaultdict
embedding_dict['prob'] = defaultdict(list)
embedding_dict['embedding'] = {}
embedding_dict['logits'] = defaultdict(list)
embedding_dict['lbl'] = {}
remainder_accuracies = []

for i in range(len(gpt_prompts[0])):
    print(i)
    try:
        curr_label_dict = {}
        for key in gpt_prompts.keys():
            curr_label_dict[key] = gpt_prompts[key][i]
        curr_acc, prompt_prob, embedding_with_keys, logits = zeroshot_classification(image_features=test_features,
                                                                            class_labels=lbl.to(device),
                                                                            prompts=curr_label_dict,
                                                                            embedding_model=embedding_model.to(device),
                                                                            model_logit=scale,
                                                                            preprocess=preprocess_frozen_model,
                                                                            model_name=fixed_embedding,
                                                                            device=device)
        remainder_accuracies.append(curr_acc)
        logits = np.array(logits.cpu())
        for j in range(len(prompt_prob)):
            embedding_dict['prob'][j].append(prompt_prob[j])
            embedding_dict['logits'][j].append(logits[j])

    except Exception as e:
        print(e)
import scipy
prob_accumulation = []
logit_accumulation = []
for i in range(len(lbl)):
    prob_accumulation.append(np.argmax(np.mean(np.stack(embedding_dict['prob'][i]), axis = 0)))
    logit_accumulation.append(np.argmax(scipy.special.softmax(np.mean(np.stack(embedding_dict['logits'][i]), axis = 0))))
embedding_dict['lbl'] = np.array(lbl.cpu())
result_dict = ({'original_accuracy': validation_accuracy,
               'gpt_accuracy':remainder_accuracies,
               'logit_accuracy': np.mean(logit_accumulation == embedding_dict['lbl']),
                'prob_accuracy': np.mean(prob_accumulation == embedding_dict['lbl'])})
with open(savepath + 'result.pickle', 'wb') as f:
    pickle.dump(result_dict, f)