import numpy as np
from PIL import Image
import torch
import os
import pickle
import csv
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
def ocelot_cell_loader(preprocess, label_dict, data_path = '/Ocelot/'):

    label_index = {}
    for key in label_dict.keys():
        label_index[label_dict[key]] = key

    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data')) + data_path
    processed = []
    labels = []
    for partition in ['train', 'val', 'test']:
        labels_path = path + 'annotations/'+partition+'/cell/'
        image_path =  path + 'images/'+partition+'/cell/'
        annotations = os.listdir(labels_path)

        for annotation in annotations:

            if '.csv' not in annotation:
                continue

            image = annotation.replace('.csv', '.jpg')
            image = Image.open(image_path+image)
            count = defaultdict(int)
            with open(labels_path + annotation, newline='') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
                for row in spamreader:
                    lbl = int(row[0].split(',')[-1])
                    count[lbl] += 1
            if count[2] > 0:
                labels.append(torch.tensor(1))
                processed.append(process(image, preprocess))
            elif count[1] > 0:
                labels.append(torch.tensor(0))
                processed.append(process(image, preprocess))
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