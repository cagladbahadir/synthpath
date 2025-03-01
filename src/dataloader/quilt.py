from PIL import Image
from torch.utils.data import Dataset
import torch
import numpy as np
import pickle
if not torch.cuda.is_available():
    import pickle5 as pickle
from collections import defaultdict
import os
from tqdm import tqdm

class quilt_dataset(Dataset):
    def __init__(self, device, preprocess_train, tokenizer, split, rewrite_count,model ):
        self.device = device
        self.path = self.set_path()
        self.images = self.get_list_of_images(split, model)
        self.quilt_dict, self.text_selection_dict = self.load_caption_dict(rewrite_count)
        self.quilt_dict_cell, self.text_selection_dict_cell = self.load_caption_dict_concept('cell')
        self.quilt_dict_disease, self.text_selection_dict_disease = self.load_caption_dict_concept('disease')
        self.quilt_dict_organ, self.text_selection_dict_organ = self.load_caption_dict_concept('organ')

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):

        exception = 1
        idx_ = idx
        while exception == 1:
            try:
                image_id = self.images[idx_]
                im = image_id[0:image_id.find('.')]
                processed_image = torch.load('Processed_Images/' + image_id)
                tokenized_text = self.select_text(im)
                tokenized_text_cell = self.select_text_cell(im)
                tokenized_text_organ = self.select_text_organ(im)
                tokenized_text_disease = self.select_text_disease(im)
                return processed_image, tokenized_text, tokenized_text_cell, tokenized_text_organ, tokenized_text_disease
            except:
                idx_+=1
    def select_text(self, im):
        if not self.text_selection_dict[im]['unused']:
            self.text_selection_dict[im]['unused'].update(self.text_selection_dict[im]['used'])
            self.text_selection_dict[im]['used'] = set()
        selected_text = np.random.choice(list(self.text_selection_dict[im]['unused']), 1)[0]
        self.text_selection_dict[im]['unused'].remove(selected_text)
        if 'used' not in self.text_selection_dict[im].keys():
            self.text_selection_dict[im]['used'] = set()
        self.text_selection_dict[im]['used'].add(selected_text)
        return self.quilt_dict[im][selected_text].to(self.device)

    def select_text_cell(self, im):
        if not self.text_selection_dict_cell[im]['unused']:
            self.text_selection_dict_cell[im]['unused'].update(self.text_selection_dict_cell[im]['used'])
            self.text_selection_dict_cell[im]['used'] = set()
        selected_text = np.random.choice(list(self.text_selection_dict_cell[im]['unused']), 1)[0]
        self.text_selection_dict_cell[im]['unused'].remove(selected_text)
        if 'used' not in self.text_selection_dict_cell[im].keys():
            self.text_selection_dict_cell[im]['used'] = set()
        self.text_selection_dict_cell[im]['used'].add(selected_text)
        return self.quilt_dict_cell[im][selected_text].to(self.device)

    def select_text_organ(self, im):
        if not self.text_selection_dict_organ[im]['unused']:
            self.text_selection_dict_organ[im]['unused'].update(self.text_selection_dict_organ[im]['used'])
            self.text_selection_dict_organ[im]['used'] = set()
        selected_text = np.random.choice(list(self.text_selection_dict_organ[im]['unused']), 1)[0]
        self.text_selection_dict_organ[im]['unused'].remove(selected_text)
        if 'used' not in self.text_selection_dict_organ[im].keys():
            self.text_selection_dict_organ[im]['used'] = set()
        self.text_selection_dict_organ[im]['used'].add(selected_text)
        return self.quilt_dict_organ[im][selected_text].to(self.device)

    def select_text_disease(self, im):
        if not self.text_selection_dict_disease[im]['unused']:
            self.text_selection_dict_disease[im]['unused'].update(self.text_selection_dict_disease[im]['used'])
            self.text_selection_dict_disease[im]['used'] = set()
        selected_text = np.random.choice(list(self.text_selection_dict_disease[im]['unused']), 1)[0]
        self.text_selection_dict_disease[im]['unused'].remove(selected_text)
        if 'used' not in self.text_selection_dict_disease[im].keys():
            self.text_selection_dict_disease[im]['used'] = set()
        self.text_selection_dict_disease[im]['used'].add(selected_text)
        return self.quilt_dict_disease[im][selected_text].to(self.device)
    def load_caption_dict(self, rewrite_count):
        with open('Processed_Text/caption_dict.pickle', 'rb') as handle:
            caption_dict = pickle.load(handle)
        with open('Processed_Text/text_selection_dict.pickle', 'rb') as handle:
            text_selection_dict = pickle.load(handle)
        count = 0
        if rewrite_count < 5:
            for im in caption_dict.keys():
                count += 1
                caption_count = len(caption_dict[im])
                caption_cut = int(np.ceil(caption_count * rewrite_count / 5 ))
                caption_dict[im] = caption_dict[im][0:caption_cut]
                text_selection_dict[im] = {'unused':set(np.arange(len(caption_dict[im])))}
                if count % 1000 == 0:
                    print(len(caption_dict[im])," / ", caption_count)
        return caption_dict, text_selection_dict

    def load_caption_dict_concept(self, concept):
        with open('Processed_Text/caption_dict_'+concept+'.pickle', 'rb') as handle:
            caption_dict = pickle.load(handle)
        with open('Processed_Text/text_selection_dict_'+concept+'.pickle', 'rb') as handle:
            text_selection_dict = pickle.load(handle)
        return caption_dict, text_selection_dict
    def build_synt_caption_dict(self):
        caption_dict = defaultdict(list)
        text_selection_dict = defaultdict(lambda: defaultdict(set))
        path = 'Mistral_language_rewrites/'
        prompt_sets = os.listdir(path)

        for prompt_set in prompt_sets:
            if '.' in prompt_set:
                continue
            batches = os.listdir(path + prompt_set)
            for batch in batches:
                if '.' in batch:
                    continue
                with open(path + prompt_set + "/" + batch + '/rewrites.pickle', 'rb') as handle:
                    rewrite = pickle.load(handle)
                list_of_keys = list(rewrite.keys())
                for key_num in range(len(list_of_keys)):
                    key = list_of_keys[key_num]
                    if key not in self.images:
                        continue
                    for caption in rewrite[key].keys():
                        text = self.filter_prompt(rewrite[key][caption])
                        tokenized_text =  self.custom_tokenize(text).to('cpu')
                        caption_dict[key].append(tokenized_text)
                        text_selection_dict[key]['unused'].add(len(caption_dict[key]) - 1)
        return caption_dict, text_selection_dict

    def process_images(self):
        images_dict = {}
        for num in range(len(self.images)):
            key = self.images[num]
            image = Image.open(os.path.join(self.path, key))
            processed_image = self.preprocess_train(image).unsqueeze(0).to('cpu')
            images_dict[key] = processed_image
        return images_dict
    def filter_prompt(self, prompt):
        prompt = prompt[0:prompt.find('.') + 1]
        return prompt
    def set_path(self):
        if self.device == 'cpu':
            path = 'Processed_Images/'
        else:
            path = 'Processed_Images/'
        return path
    def get_list_of_images(self, split, model):
        list_of_images = os.listdir(self.path)
        if split == 'train':
            list_of_images = list_of_images[0: int(len(list_of_images) * 0.85)]
        else:
            list_of_images = list_of_images[int(len(list_of_images) * 0.85):]
        if not torch.cuda.is_available():
            list_of_images = list_of_images[0:32]
        return list_of_images

    def custom_tokenize(self, text):
        cut = len(text)
        exception = True
        while exception:
            try:
                tokenized = self.tokenizer(text[0:cut])
                exception = False
            except:
                cut -= 10
        return tokenized

def custom_collate(original_batch):
    image_tensor = []
    text_tokens = []
    text_token_cell = []
    text_token_organ = []
    text_token_disease = []
    for i in range(len(original_batch)):
        image_tensor.append(original_batch[i][0])
        text_tokens.append(original_batch[i][1])
        text_token_cell.append(original_batch[i][2])
        text_token_organ.append(original_batch[i][3])
        text_token_disease.append(original_batch[i][4])


    image_tensor = torch.vstack(image_tensor)
    text_tokens = torch.vstack(text_tokens)
    text_token_cell  = torch.vstack(text_token_cell)
    text_token_organ  = torch.vstack(text_token_organ)
    text_token_disease = torch.vstack(text_token_disease)
    return image_tensor, text_tokens, text_token_cell, text_token_organ, text_token_disease