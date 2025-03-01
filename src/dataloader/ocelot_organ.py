import numpy as np
from PIL import Image
import torch
import os
import pickle
import csv
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
import json
def ocelot_organ_loader(location, preprocess, label_dict):

    if location != 'cpu':
        path = '/share/sablab/nfs04/data/Path_CLIP/Ocelot/'
    else:
        path = '/Users/caglabahadir/Desktop/PATH_CLIP/Ocelot/'
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data')) + data_path
    label_keys = {}
    for key in label_dict.keys():
        label_keys[label_dict[key]] = key

    f = open(path + '/metadata.json')
    data = json.load(f)
    tissue_dict = {}
    for sample in data['sample_pairs'].keys():
        tissue_dict[sample] = data['sample_pairs'][sample]['organ']
    f.close()

    processed = []
    labels = []
    for partition in ['train', 'val', 'test']:
        image_path =  path + 'images/'+partition+'/tissue/'
        images = os.listdir(image_path)

        for image in images:
            if '.jpg' not in image:
                continue
            image_read = Image.open(image_path+image)
            processed.append(process(image_read, preprocess))
            labels.append(torch.tensor(label_keys[tissue_dict[image.replace('.jpg','')]]))
    processed = torch.vstack(processed)
    labels = torch.stack(labels)
    return processed, labels


def process(im, preprocess):
    try:
        im = preprocess(Image.fromarray(np.uint8(im))).unsqueeze(0)
    except:
        im = preprocess(text=[''], images=Image.fromarray(np.uint8(im)), return_tensors="pt", padding=True).data[
            'pixel_values'][0]
        im = im.unsqueeze(0)
    return im