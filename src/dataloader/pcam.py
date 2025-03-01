import numpy as np
from PIL import Image
import torch
import os
import csv
import h5py

def camelyon_loader( preprocess, data_path = 'PatchCamelyon/'):
    #label_dict = {0: "lymph node", 1: "lymph node containing metastatic tumor tissue"}


    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data')) + data_path
    f = h5py.File(path + 'camelyonpatch_level_2_split_test_x.h5', 'r')
    x = f['x']
    f = h5py.File(path + 'camelyonpatch_level_2_split_test_y.h5', 'r')
    y = f['y']
    processed = []
    labels = []
    length = len(x)

    for i in range(length):
        im = x[i]
        try:
            im = preprocess(Image.fromarray(np.uint8(im))).unsqueeze(0)
            processed.append(im)
        except:
            im = preprocess(text=[''], images=Image.fromarray(np.uint8(im)), return_tensors="pt", padding=True).data['pixel_values'][0]
            processed.append(im.unsqueeze(0))
        labels.append(torch.tensor(y[i].item()))
    processed = torch.vstack(processed)
    labels = torch.stack(labels)
    return processed, labels
