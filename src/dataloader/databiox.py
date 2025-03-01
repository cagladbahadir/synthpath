import h5py
import numpy as np
from PIL import Image
import torch
import os
def databiox_loader(preprocess, data_path = '/databiox'):
    # label_dict = { 0: "well differentiated bloom richardson grade one",
    #            1: "moderately differentiated bloom richardson grade two",
    #            2: "poorly differentiated grade three"}

    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data')) + data_path
    classes = {'BreastCancer_IDC_Grade_1': 0, 'BreastCancer_IDC_Grade_2': 1, 'BreastCancer_IDC_Grade_3': 2}

    processed = []
    labels = []
    for cls in classes.keys():
        imlist = os.listdir(path + cls +"/"+ cls.replace('BreastCancer', 'BC')+"\\20x/")
        for i in range(len(imlist)):
            if imlist[i].endswith('JPG') or imlist[i].endswith('jpg'):
                im = Image.open(path + cls +"/"+ cls.replace('BreastCancer', 'BC')+"\\20x/" + imlist[i])
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