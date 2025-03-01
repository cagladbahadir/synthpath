from transformers import AutoModelForCausalLM, AutoTokenizer
import time
import argparse
from collections import defaultdict
from tqdm import tqdm
import os
import pickle
def parser_func():
    ## Training time
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", default='ocelot_cell')
    parser.add_argument("--length", default = 'long')
    parser.add_argument("--savepath", default='')
    return parser
parser = parser_func()
args = parser.parse_args()
device = "cuda:0" # the device to load the model onto
savepath = args.savepath
if args.length == 'long':
    from mistral_message_templates.lc_lung import message_lclung
    from mistral_message_templates.lc_colon import message_lccolon
    from mistral_message_templates.skin_cancer import message_skincancer
    from mistral_message_templates.skin_tumor import message_skintumor
    from mistral_message_templates.pcam import message_pcam
    from mistral_message_templates.bach import message_bach
    from mistral_message_templates.renal_cell import message_renal_cell
    from mistral_message_templates.osteo import message_osteo
    from mistral_message_templates.mhist import message_mhist
    from mistral_message_templates.nck_crc import message_nck_crc
    from mistral_message_templates.sicap import message_sicap
    from mistral_message_templates.databiox import message_databiox
    from mistral_message_templates.pannuke_organ import message_pannukeorgan
    from mistral_message_templates.pannuke_cell import message_pannuke_cell
    from mistral_message_templates.ocelot_organ import message_ocelot_organ
    from mistral_message_templates.ocelot_cell import message_ocelot_cell
else:
    from mistral_short_message_templates.lc_lung import message_lclung
    from mistral_short_message_templates.lc_colon import message_lccolon
    from mistral_short_message_templates.skin_cancer import message_skincancer
    from mistral_short_message_templates.skin_tumor import message_skintumor
    from mistral_short_message_templates.pcam import message_pcam
    from mistral_short_message_templates.bach import message_bach
    from mistral_short_message_templates.renal_cell import message_renal_cell
    from mistral_short_message_templates.osteo import message_osteo
    from mistral_short_message_templates.mhist import message_mhist
    from mistral_short_message_templates.nck_crc import message_nck_crc
    from mistral_short_message_templates.sicap import message_sicap
    from mistral_short_message_templates.databiox import message_databiox
    from mistral_short_message_templates.pannuke_organ import message_pannukeorgan
    from mistral_short_message_templates.ocelot_organ import message_ocelot_organ
    from mistral_short_message_templates.ocelot_cell import message_ocelot_cell
    from mistral_short_message_templates.pannuke_cell import message_pannuke_cell

t0 = time.time()
result_dict = defaultdict(dict)
if args.dataset == 'lc_lung':
    messages_dict = message_lclung()
elif args.dataset == 'lc_colon':
    messages_dict = message_lccolon()
elif args.dataset == 'skin_cancer':
    messages_dict = message_skincancer()
elif args.dataset == 'skin_tumor':
    messages_dict = message_skintumor()
elif args.dataset == 'pcam':
    messages_dict = message_pcam()
elif args.dataset == 'bach':
    messages_dict = message_bach()
elif args.dataset == 'renal_cell':
    messages_dict = message_renal_cell()
elif args.dataset == 'osteo':
    messages_dict = message_osteo()
elif args.dataset == 'mhist':
    messages_dict = message_mhist()
elif args.dataset == 'crc':
    messages_dict = message_nck_crc()
elif args.dataset == 'sicap':
    messages_dict = message_sicap()
elif args.dataset == 'databiox':
    messages_dict = message_databiox()
elif args.dataset == 'pannuke_organ':
    messages_dict = message_pannukeorgan()
elif args.dataset == 'ocelot_organ':
    messages_dict = message_ocelot_organ()
elif args.dataset == 'ocelot_cell':
    messages_dict = message_ocelot_cell()
elif args.dataset == 'pannuke_cell':
    messages_dict = message_pannuke_cell()
model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2")
tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2")

if not os.path.isdir(savepath): os.makedirs(savepath)

for k in tqdm(range(1000)):
    for cls in messages_dict.keys():
        messages = messages_dict[cls]
        encodeds = tokenizer.apply_chat_template(messages, return_tensors="pt")
        model_inputs = encodeds.to(device)
        model.to(device)

        generated_ids = model.generate(model_inputs, max_new_tokens=1000, do_sample=True)
        decoded = tokenizer.batch_decode(generated_ids)

        start = decoded[0].rfind('[/INST]') + 7
        end =  decoded[0].rfind('</s>')

        result = decoded[0][start:end]
        result_dict[cls][k] = result
        print(cls, result)
        with open(savepath + 'prompts.pickle', 'wb') as handle:
            pickle.dump(result_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
