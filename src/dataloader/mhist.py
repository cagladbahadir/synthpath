import numpy as np
from PIL import Image
import torch
import os
import csv

def mhist_loader(preprocess, data_path = '/MHIST/'):
    #label_dict = {0: "hyperplastic polyp", 1: "sessile serrated adenoma"}

    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data')) + data_path
    x = os.listdir(path+'/images/')
    y = {}
    with open(path+'annotations.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            y[row['Image Name']] = row['Majority Vote Label']
    processed = []
    labels = []
    length = len(x)
    for i in range(length):
        im = Image.open(path +'images/'+ x[i])
        try:
            im = preprocess(Image.fromarray(np.uint8(im))).unsqueeze(0)
            processed.append(im)
        except:
            im = preprocess(text=[''], images=Image.fromarray(np.uint8(im)), return_tensors="pt", padding=True).data['pixel_values'][0]
            processed.append(im.unsqueeze(0))
        if y[x[i]] == 'HP':
            lbl = 0
        elif y[x[i]] == 'SSA':
            lbl = 1
        labels.append(torch.tensor(lbl))
    processed = torch.vstack(processed)
    labels = torch.stack(labels)
    return processed, labels