import numpy as np
from PIL import Image
import torch
import os

def lc_lung_loader(preprocess, data_path = '/lung_colon_image_set/lung_image_sets/'):
    # label_dict = {0: "lung adenocarcinoma",
    #               1: "benign lung",
    #               2: "lung squamous cell carcinoma"}
    classes = {'lung_aca': 0,  'lung_n': 1, 'lung_scc': 2}
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data')) + data_path
    processed = []
    labels = []
    for cls in classes.keys():
        x = os.listdir(path + cls)
        for i in range(len(x)):
            if not x[i].endswith('.jpeg'):
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