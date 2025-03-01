import numpy as np
from PIL import Image
import torch
import os
def crc_loader(preprocess, data_path ='/CRC-VAL-HE-7K/' ):
    # label_dict = {0: "adipose",
    #               1: "debris",
    #               2: "lymphocytes",
    #               3: "mucus",
    #               4: "smooth muscle",
    #               5: "normal colon mucosa",
    #               6: "cancer associated stroma",
    #               7: "colorectal adenocarcinoma epithelium"
    #               }

    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data')) + data_path
    classes = {'ADI': 0, 'DEB': 1, 'LYM': 2, 'MUC': 3, 'MUS':4, 'NORM':5,'STR':6, 'TUM':7}
    processed = []
    labels = []
    for cls in classes.keys():
        imlist = os.listdir(path + cls)
        for i in range(len(imlist)):
            if imlist[i].endswith('tif'):
                im = Image.open(path  + "/" + cls+"/" + imlist[i])
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