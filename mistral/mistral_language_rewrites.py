from transformers import AutoModelForCausalLM, AutoTokenizer
import time
import argparse
from collections import defaultdict
from tqdm import tqdm
import os
import pickle
import numpy as np
import copy

import warnings

warnings.filterwarnings("ignore")


def parser_func():
    ## Training time
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", default=1)
    parser.add_argument("--batch", default=0)
    return parser


parser = parser_func()
args = parser.parse_args()

device = "cuda:0"  # the device to load the model onto
model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2")
tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2")

savepath = 'Mistral_language_rewrites/Prompt_' + str(args.prompt) + '/Batch_' + str(args.batch) + "/"
if not os.path.isdir(savepath): os.makedirs(savepath)

with open('Quilt/quilt_dict.pickle', 'rb') as handle:
    quilt = pickle.load(handle)

# Divide to keys
list_of_keys = list(quilt.keys())
batch_size = int(len(list_of_keys) / 8)
keys = list_of_keys[int(args.batch) * batch_size: (int(args.batch) + 1) * batch_size]

# General rewrites
prompt_dict = {0: [
    {"role": "user", "content": "You are a pathologist. Can you rephrase the following sentence? This sentence is imperfect and might have non-sensical words, please ignore those words. Feel free to use synonyms and additional pathology knowledge about the medical terms. \n \
                   Sentence to be rephrased: Peritoneum, Day 4 These two biopsies (1 & 2) were taken from the same patient. What is your DailyDx of each of these peritoneal biopsies? What other finding is most likely to be present in this patient? Answers & quick facts tomorrow! UMichPath SurgPath."},
    {"role": "assistant", "content": "What can be said regarding the peritoneal biopsy of this patient?"},
    {"role": "user", "content": "Can you rephrase this sentence? \
                   Sentence to be rephrased: Teenager with a large hemispheric tumor.'PNET'-like morphology, with Olig2 negative and ATRX loss. What is the most likely diagnosis?PathTwitter neuropath neurotwitter"},
    {"role": "assistant",
     "content": "ATRX, a chromatin remodeler protein, is recurrently mutated in H3F3A-mutant pediatric glioblastoma."},
    {"role": "user", "content": "Can you rephrase this sentence? \
                   Sentence to be rephrased: Nephrogenic systemic fibrosis is a fibrotic disorder with deep involvement that goes down to the fascia."},
    {"role": "assistant",
     "content": "Nephrogenic systemic fibrosis is a rare disease that occurs mainly in people with advanced kidney failure with or without dialysis."},
    {"role": "user", "content": "Can you rephrase this sentence? \
                   Sentence to be rephrased: [INSERT_SENTENCE_HERE]"}
]
}

# Organ context
prompt_dict[1] = [
    {"role": "user", "content": "You are a pathologist. Can you infer which organ the sentence is referring to and write a sentence describing a pathology image coming from that particular organ?. \n \
                   Input sentence: Peritoneum, Day 4 These two biopsies (1 & 2) were taken from the same patient. What is your DailyDx of each of these peritoneal biopsies? What other finding is most likely to be present in this patient? Answers & quick facts tomorrow! UMichPath SurgPath."},
    {"role": "assistant", "content": "This is an H&E slide from the peritoneum."},
    {"role": "user", "content": "Can you infer the organ from this sentence and write a new sentence? \
                   Input sentence: Teenager with a large hemispheric tumor.'PNET'-like morphology, with Olig2 negative and ATRX loss. What is the most likely diagnosis?PathTwitter neuropath neurotwitter"},
    {"role": "assistant",
     "content": "Brain tissue is clearly seen in this pathology slide."},
    {"role": "user", "content": "Can you infer the organ from this sentence and write a new sentence? \
                   Input sentence: Nephrogenic systemic fibrosis is a fibrotic disorder with deep involvement that goes down to the fascia."},
    {"role": "assistant",
     "content": "Patient's kidney sample is under the microscope."},
    {"role": "user", "content": "Can you infer the organ from this sentence and write a new sentence? \
                   Input sentence: [INSERT_SENTENCE_HERE]"}
]

def disease_prompt():
    question_1 = "You are a pathologist, who can understand if a sentence is talking about the presence \
            of a disease in a pathology image. The sentence may have indications such as the mention of some \
            genetic markers like gene mutations, or some morphological information regarding tumor presence. \
            Your role is to categorize the sentence as talking about 'diseased', or 'normal' pathology\
            image.Can you infer if the sentence talks about \
            presence of a disease or not from the sentence below? \
            If the sentence talks about any particular disease, output 'diseased'.\
            Only output 'normal' if the sentence does not describe a pathology or\
            it says that the features are not evident of disease.\
            Please limit your answer to one word from the list: \
            diseased and normal. \n"
    question_rest = "Can you infer if the sentence talks about presence or description of a disease \
                or its lack thereof from the sentence below? \
                Please limit your answer to one word from the list: diseased and normal. \n"
    disease_prompt_sentences = [
        {"role": "user", "content": question_1 +
                                    "Sentence: Peritoneum, Day 4 These two biopsies (1 & 2) were taken from the same patient.\
                                    What is your DailyDx of each of these peritoneal biopsies? \
                                    What other finding is most likely to be present in this patient? \
                                    Answers & quick facts tomorrow! UMichPath SurgPath."},

        {"role": "assistant", "content": "normal \n \
        Explanation: Biopsy results are unclear."},

        {"role": "user", "content": question_rest +
                                    "Sentence: Teenager with a large hemispheric tumor.'PNET'-like morphology, with Olig2 negative and ATRX loss. What is the most likely diagnosis?PathTwitter neuropath neurotwitter"},

        {"role": "assistant", "content": "diseased \n \
        Explanation: The disease is the hemispheric tumor."},

        {"role": "user", "content": question_rest +
                                    "Sentence: Nephrogenic systemic fibrosis is a fibrotic disorder with deep involvement that goes down to the fascia."},

        {"role": "assistant", "content": "diseased \n \
        Explanation: The disease is the nephrogenic systemic fibrosis."},

        {"role": "user", "content": question_rest +
                                    "Sentence: The breast tissue shows hyperplasia, which is a normal finding in pregnancy."},

        {"role": "assistant", "content": "normal \n \
        Explanation: Sentence mentions that the hyperplasia is normal in pregnancy."},

        {"role": "user", "content": question_rest +
                                    "Sentence The immunocytochemistry of IDH1 in MG63 and U2OS. \
                                    IDH1 is specifically detected in the cytoplasm of both osteosarcoma cell lines MG63 and U2OS.\
                                    (A) Expression of IDH1 in U2OS, × 200; (B) Expression of IDH1 in MG63,× 200; \
                                    (C) Expression of IDH1 in U2OS,× 400; (D) Expression of IDH1 in MG63,× 400."
         },

        {"role": "assistant", "content": "diseased \n \
        Explanation: IDH is a gene that is present in osteosarcoma which is a type of cancer. In (A)\
        it mentions that the IDH is expressed."},
        {"role": "user", "content": question_rest +
                                    "Sentence: [INSERT_SENTENCE_HERE] "}
    ]

    return disease_prompt_sentences


prompt_dict[2] = disease_prompt()

def cell_prompt():
    question_1 = """You are a pathologist. Your job is to extract cell related information from a sentence. \ 
                 You should identify cell names mentioned in the sentence and output them. \
                 If there is no cell related information, output 'None'. \
                 Do not exceed 10 words.\n"""
    question_rest = "Can you extract cell related information from the sentence below? \
                    If no cell information is present, output 'None'. \
                    Do not exceed 10 words. \n"
    cell_prompts = [
            {"role": "user", "content": question_1 +
                                        "Sentence: The cells outlined in green form the acini of the \
                                        pancreas and the blue arrow indicates a centroacinar cell."},

            {"role": "assistant", "content": "Centroacinar cells."},  # are spindle-shaped cells."},

            {"role": "user", "content": question_rest +
                                        "Sentence:  Esophageal biopsy shows eosinophils and basal zone hyperplasia."},

            {"role": "assistant", "content": "Eosinophils."},  # " are a type of white blood cell."},

            {"role": "user", "content": question_rest +
                                        "Sentence: Pigmented lesion from the floor of the mouth with a previous history of melanoma. What is your diagnosis of this pigmented lesion?? UForalpath headandneckpath UF HandNpathology ENTpath."},

            {"role": "assistant", "content": "None"},

            {"role": "user", "content": question_rest +
                                        "Sentence:  Tumor of lingual dorsum in a 59 y-o male. \
                                        Ulcerated epithelium replaced by a thick fibrinopurulent membrane (1) \
                                        and a underlying band of acute inflammatory cells (2). \
                                        A granulation-like tissue form the bulk of the tumor (3), \
                                        with proliferation of endothelial cells (4). oralpath"},

            {"role": "assistant", "content": "Acute inflammatory cells and \
            proliferating (multiplying) endothelial cells."},

            {"role": "user", "content": question_rest +
                                        "Sentence: Renal bx in the setting of multicentric castleman/TAFRO syndrome. \
                                        Glomerular limited chronic active microangiopathy. \
                                        GBM double contours/remodeling and endotheliosis.  renalpath"},

            {"role": "assistant", "content": "None"},

            {"role": "user", "content": question_rest +
                                        "Sentence: Description of the anatomy of the adrenal gland, including the capsule, cortex, and medulla."},

            {"role": "assistant", "content": "None"},

            {"role": "user", "content": question_rest +
                                        "Sentence: The presence of large myxoid-chondroidy nodules and sweat ducts \
                                        embedded in myxoid stroma suggests a mixed tumor or chondroid syringoma."},

            {"role": "assistant", "content": "None"},

            {"role": "user", "content": question_rest +
                                        "Sentence: Discussion of small cell carcinoma and its characteristics."},

            {"role": "assistant", "content": "None"},

            {"role": "user", "content": question_rest +
                                        "Sentence: This one is a bit trickier, but still classy! conchal cymba lesion. \
                                       Look how pagetoid those cells are! Ddx? And whats your bet?Dermpath pathology dermatology dermtwitter"},

            {"role": "assistant", "content": "Pagetoid cells."},

            {"role": "user", "content": question_rest +
                                        "Sentence: [INSERT_SENTENCE_HERE] "}
        ]
    return cell_prompts

prompt_dict[3] = cell_prompt()

if int(args.prompt) == 3:
    with open(savepath + 'rewrites.pickle', 'rb') as handle:
        language_rewrites = pickle.load(handle)
else:
    language_rewrites = {}
count = -1
t0 = time.time()
completed_keys = list(language_rewrites.keys())
for key in keys:
    count += 1
    if key in completed_keys and len(language_rewrites[key].keys()) == len(quilt[key]['caption'].keys()):
        continue
    result_dict = {}
    for caption_key in quilt[key]['caption']:
        caption = quilt[key]['caption'][caption_key].replace('"', "'")
        if int(args.prompt) == 6 or int(args.prompt) == 7:
            sentences = ''
            for capt_key in quilt[key]['caption'].keys():
                sentences += quilt[key]['caption'][caption_key].replace('"', "'") + ' '
            caption = sentences

        copied_dict = copy.deepcopy(prompt_dict)
        messages = copied_dict[int(args.prompt)]
        messages[-1]['content'] = messages[-1]['content'].replace('[INSERT_SENTENCE_HERE]', caption)
        encodeds = tokenizer.apply_chat_template(messages, return_tensors="pt")

        model_inputs = encodeds.to(device)
        model.to(device)

        generated_ids = model.generate(model_inputs, max_new_tokens=1000, do_sample=True)
        decoded = tokenizer.batch_decode(generated_ids)
        start = decoded[0].rfind('[/INST]') + 7
        end = decoded[0].rfind('</s>')

        result = decoded[0][start:end]
        result_dict[caption_key] = result

    language_rewrites[key] = result_dict

    if count % 100 == 0:
        print(np.around(count / len(keys), decimals=4), '% complete in ',
              np.around((time.time() - t0) / 60, decimals=2), ' minutes.')
        with open(savepath + 'rewrites.pickle', 'wb') as handle:
            pickle.dump(language_rewrites, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open(savepath + 'rewrites.pickle', 'wb') as handle:
    pickle.dump(language_rewrites, handle, protocol=pickle.HIGHEST_PROTOCOL)
