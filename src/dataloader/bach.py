import numpy as np
from PIL import Image
import torch
import os
def bach_loader(preprocess, data_path = '/ICIAR_BACH/ICIAR2018_BACH_Challenge/Photos/'):
    # label_dict = {0: "breast non-malignant benign tissue",
    #               1: "breast malignant in-situ carcinoma",
    #               2: "breast malignant invasive carcinoma",
    #               3: "breast normal breast tissue"}
    classes = {'Benign': 0, 'InSitu': 1, 'Invasive': 2, 'Normal': 3}
    processed = []
    labels = []
    path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..','..', 'data')) + data_path

    for cls in classes.keys():
        x = os.listdir(path + cls)
        for i in range(len(x)):
            if not x[i].endswith('.tif'):
                continue
            im = Image.open(path + cls + '/' + x[i])
            try:
                im = preprocess(Image.fromarray(np.uint8(im))).unsqueeze(0)
                processed.append(im)
            except:
                im = \
                preprocess(text=[''], images=Image.fromarray(np.uint8(im)), return_tensors="pt", padding=True).data[
                    'pixel_values'][0]
                processed.append(im.unsqueeze(0))
            labels.append(torch.tensor(classes[cls]))
    processed = torch.vstack(processed)
    labels = torch.stack(labels)
    return processed, labels
