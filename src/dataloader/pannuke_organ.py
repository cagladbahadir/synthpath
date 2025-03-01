import numpy as np
from PIL import Image
import torch
import os
import pickle
def pannuke_organ_loader(location, preprocess, label_dict):

    label_index = {}
    for key in label_dict.keys():
        label_index[label_dict[key]] = key
    if location != 'cpu':
        path = '/share/sablab/nfs04/data/Path_CLIP/PanNuke/processed/'
    else:
        path = '/Users/caglabahadir/Desktop/PATH_CLIP/PanNuke/processed/'
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data')) + data_path
    processed = []
    labels = []
    folds = ['fold1', 'fold2', 'fold3']
    for fold in folds:
        with open(path + fold + '/labels/labels_dict.pickle', 'rb') as f:
            lbl = pickle.load(f)
        #images = os.listdir(path + fold + '/images/')
        for i in lbl.keys():
            im = np.load(path + fold + '/images/' + i +'.npy')
            try:
                im = preprocess(Image.fromarray(np.uint8(im))).unsqueeze(0)
                processed.append(im)
            except:
                im = \
                preprocess(text=[''], images=Image.fromarray(np.uint8(im)), return_tensors="pt", padding=True).data[
                    'pixel_values'][0]
                processed.append(im.unsqueeze(0))
            labels.append(torch.tensor(label_index[lbl[i]['tissue_type'].replace('-', ' ').replace('_',' ')]))
    processed = torch.vstack(processed)
    labels = torch.stack(labels)
    if not torch.cuda.is_available():
        processed = processed[0:10]
        labels = labels[0:10]
    return processed, labels