import numpy as np
from PIL import Image
import torch
import os

def skin_tumor_loader(preprocess, data_path = 'skincancer/tiles/'):
    # label_dict = {0: "squamous cell carcinoma",
    # 1: "melanoma in situ",
    # 2: "basal cell carcinoma",
    # 3: "naevus"}

    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data')) + data_path

    classes = {'tumor_skin_epithelial_sqcc': 0,
               'tumor_skin_melanoma_melanoma': 1,
               'tumor_skin_epithelial_bcc': 2,
               'tumor_skin_naevus_naevus': 3}
    processed = []
    labels = []
    for cls in classes.keys():
        x = os.listdir(path + cls)
        for i in range(len(x)): # x[0:500]
            if not x[i].endswith('.jpg'):
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