import h5py
import numpy as np
from PIL import Image
import torch
import os

def skin_cancer_loader(preprocess, data_path = 'skincancer/tiles/'):
    # label_dict = {0: "necrosis",
    #          1: "skeletal muscle",
    #          2: "eccrine sweat glands",
    #          3: "vessels",
    #          4: "elastosis",
    #          5: "chondral tissue",
    #          6: "hair follicle",
    #          7: "epidermis",
    #          8: "nerves",
    #          9: "subcutis",
    #          10: "dermis",
    #          11: "sebaceous glands",
    #          12: "squamous-cell carcinoma",
    #          13: "melanoma in-situ",
    #          14: "basal-cell carcinoma",
    #          15: "naevus"}
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data')) + data_path
    classes = {'nontumor_skin_necrosis_necrosis': 0,
               'nontumor_skin_muscle_skeletal': 1,
               'nontumor_skin_sweatglands_sweatglands': 2,
               'nontumor_skin_vessel_vessel': 3,
               'nontumor_skin_elastosis_elastosis': 4,
               'nontumor_skin_chondraltissue_chondraltissue':5,
               'nontumor_skin_hairfollicle_hairfollicle':6,
               'nontumor_skin_epidermis_epidermis':7,
               'nontumor_skin_nerves_nerves':8,
               'nontumor_skin_subcutis_subcutis':9,
               'nontumor_skin_dermis_dermis':10,
               'nontumor_skin_sebaceousglands_sebaceousglands':11,
               'tumor_skin_epithelial_sqcc': 12,
               'tumor_skin_melanoma_melanoma': 13,
               'tumor_skin_epithelial_bcc': 14,
               'tumor_skin_naevus_naevus': 15}
    processed = []
    labels = []
    for cls in classes.keys():
        x = os.listdir(path + cls)
        for i in range(len(x)): # len(x[0:500])
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