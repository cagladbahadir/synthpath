import torch
from collections import defaultdict
import os
if torch.cuda.is_available():
    import pickle
else:
    import pickle5 as pickle

def prompt_process(prompts):
    processed_prompts = defaultdict(list)
    for key in prompts.keys():
        for caption_id in prompts[key]:
            caption = prompts[key][caption_id]
            processed_prompts[key].append(caption[0:caption.find('.') + 1])
    return processed_prompts
def mistral_test_prompt_read(dataset):
    processed_final = defaultdict(list)
    folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data/test_prompts/'))
    paths = [folder_path + '/Mistral_long_prompts/',folder_path + '/Mistral_short_prompts/']
    for path in paths:
        if dataset == 'LC_Lung':
            with open(path + 'lc_lung/prompts.pickle', 'rb') as handle:
                prompts = pickle.load(handle)
        elif dataset == 'MHIST':
            with open(path + 'mhist/prompts.pickle', 'rb') as handle:
                prompts = pickle.load(handle)
        elif dataset == 'LC_Colon':
            with open(path + 'lc_colon/prompts.pickle', 'rb') as handle:
                prompts = pickle.load(handle)
        elif dataset == 'BACH':
            with open(path + 'bach/prompts.pickle', 'rb') as handle:
                prompts = pickle.load(handle)
        elif dataset == 'CRC':
            with open(path + 'crc/prompts.pickle', 'rb') as handle:
                prompts = pickle.load(handle)
        elif dataset == 'Databiox':
            with open(path + 'databiox/prompts.pickle', 'rb') as handle:
                prompts = pickle.load(handle)
        elif dataset == 'SICAP':
            with open(path + 'sicap/prompts.pickle', 'rb') as handle:
                prompts = pickle.load(handle)
        elif dataset == 'Renal_cell':
            with open(path + 'renal_cell/prompts.pickle', 'rb') as handle:
                prompts = pickle.load(handle)
        elif dataset == 'Skin_cancer':
            with open(path + 'skin_cancer/prompts.pickle', 'rb') as handle:
                prompts = pickle.load(handle)
        elif dataset == 'Skin_tumor':
            with open(path + 'skin_tumor/prompts.pickle', 'rb') as handle:
                prompts = pickle.load(handle)
        elif dataset == 'Osteo':
            with open(path + 'osteo/prompts.pickle', 'rb') as handle:
                prompts = pickle.load(handle)
        elif dataset == 'Camelyon':
            with open(path + 'pcam/prompts.pickle', 'rb') as handle:
                prompts = pickle.load(handle)
        elif dataset == 'Pannuke_Organ':
            with open(path + 'pannuke_organ/prompts.pickle', 'rb') as handle:
                prompts = pickle.load(handle)
        elif dataset == 'Pannuke_Cell':
            with open(path + 'pannuke_cell/prompts.pickle', 'rb') as handle:
                prompts = pickle.load(handle)
        elif dataset == 'Ocelot_Cell':
            with open(path + 'ocelot_cell/prompts.pickle', 'rb') as handle:
                prompts = pickle.load(handle)
        elif dataset == 'Ocelot_Organ':
            with open(path + 'ocelot_organ/prompts.pickle', 'rb') as handle:
                prompts = pickle.load(handle)
        processed = prompt_process(prompts)
        for i in processed.keys():
            processed_final[i].extend(processed[i])
    return processed_final


