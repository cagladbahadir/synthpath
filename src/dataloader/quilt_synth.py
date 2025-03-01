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

class quilt_synth_dataset(Dataset):
    def __init__(self, device, preprocess_train, tokenizer, split, args ):
        self.device = device
        self.args = args
        self.path = self.set_path()
        self.images = self.get_list_of_images(split)
        self.quilt_dict_cell, self.text_selection_dict_cell = self.load_caption_dict_concept('cell')
        self.quilt_dict_disease, self.text_selection_dict_disease = self.load_caption_dict_concept('disease')
        self.quilt_dict_organ, self.text_selection_dict_organ = self.load_caption_dict_concept('organ')

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):

        image_id = self.images[idx]
        if self.args.subtype == 'B-16':
            path = 'Processed_Image_Representations_Synth_Net_B16/'
        elif self.args.subtype == 'B-32':
            path = 'Processed_Image_Representations_Synth_Net/'

        processed_image = torch.load(path + image_id+'.pt')
        tokenized_text_cell = self.select_text_cell(image_id)
        tokenized_text_organ = self.select_text_organ(image_id)
        tokenized_text_disease = self.select_text_disease(image_id)
        return processed_image, tokenized_text_cell, tokenized_text_organ, tokenized_text_disease


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

    def load_caption_dict_concept(self, concept):
        if self.args.subtype == 'B-16':
            path = 'Text_Representations_Synth_Net_B16/'
        elif self.args.subtype == 'B-32':
            path = 'Text_Representations_Synth_Net/'

        with open(path+'caption_dict_'+concept+'.pickle', 'rb') as handle:
            caption_dict = pickle.load(handle)
        with open('Processed_Text/text_selection_dict_'+concept+'.pickle', 'rb') as handle:
            text_selection_dict = pickle.load(handle)
        return caption_dict, text_selection_dict

    def set_path(self):
        if self.args.subtype == 'B-16':
            path = 'Processed_Image_Representations_Synth_Net_B16/'
        elif self.args.subtype == 'B-32':
            path = 'Processed_Image_Representations_Synth_Net/'
        return path
    def get_list_of_images(self, split):
        if self.args.subtype == 'B-16':
            path = 'Text_Representations_Synth_Net_B16/'
        elif self.args.subtype == 'B-32':
            path = 'Text_Representations_Synth_Net/'

        with open(path+'caption_dict_cell.pickle', 'rb') as handle:
            caption_dict = pickle.load(handle)
        list_of_images = list(caption_dict.keys())
        if split == 'train':
            list_of_images = list_of_images[0: int(len(list_of_images) * 0.85)]
        else:
            list_of_images = list_of_images[int(len(list_of_images) * 0.85):]
        if not torch.cuda.is_available():
            list_of_images = list_of_images[0:32]
        return list_of_images

def custom_collate_synth(original_batch):
    image_tensor = []
    text_token_cell = []
    text_token_organ = []
    text_token_disease = []
    for i in range(len(original_batch)):
        image_tensor.append(original_batch[i][0])
        text_token_cell.append(original_batch[i][1])
        text_token_organ.append(original_batch[i][2])
        text_token_disease.append(original_batch[i][3])
    image_tensor = torch.vstack(image_tensor)
    text_token_cell  = torch.vstack(text_token_cell)
    text_token_organ  = torch.vstack(text_token_organ)
    text_token_disease = torch.vstack(text_token_disease)
    return image_tensor, text_token_cell, text_token_organ, text_token_disease