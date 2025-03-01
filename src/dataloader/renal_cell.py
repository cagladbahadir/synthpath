import numpy as np
from PIL import Image
import torch
import os
def renal_cell_loader(preprocess, data_path = 'renal_cell/'):
    # label_dict = {0: "red blood cells",
    #               1: "renal cancer",
    #               2: "normal renal tissue",
    #               3: "torn adipose necrotic tissue",
    #               4: "muscle fibrous stroma blood vessels"}
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data')) + data_path
    classes = {'blood': 0,  'cancer': 1, 'normal': 2, 'other': 3, 'stroma': 4}
    processed = []
    labels = []
    for cls in classes.keys():
        x = os.listdir(path + cls)
        for i in range(len(x)): # len(x[0:500])
            if not x[i].endswith('.png'):
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