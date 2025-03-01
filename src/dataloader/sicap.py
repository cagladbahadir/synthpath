import numpy as np
from PIL import Image
import torch
import csv
from collections import defaultdict
import os
def sicap_loader(preprocess, data_path = 'SICAPv2/'):
    # "sicap": ["benign glands", NC
    #           "atrophic dense glands", #G3
    #           "cribriform ill-formed fused papillary patterns", #G4
    #           "isolated nest cells without lumen roseting patterns" #G5
    #           ],
    # label_dict = { 0: "benign glands",
    #                1: "atrophic dense glands",
    #                2: "cribriform ill-formed fused papillary patterns",
    #                3: "isolated nest cells without lumen roseting patterns"}

    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data')) + data_path
    classes = {'NC': 0, 'G3': 1, 'G4': 2, 'G5': 3}
    image_dict = defaultdict(list)
    with open(path+'partition/Test/Test.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            image_path = row['\ufeffimage_name']
            if row['NC'] == '1':
                image_dict['NC'].append(image_path)
            elif row['G3'] == '1':
                image_dict['G3'].append(image_path)
            elif row['G4'] == '1':
                image_dict['G4'].append(image_path)
            elif row['G5'] == '1':
                image_dict['G5'].append(image_path)

    processed = []
    labels = []
    for cls in classes.keys():
        imlist = image_dict[cls]
        for i in range(len(imlist)):
            im = Image.open(path  + '/images/' + imlist[i])
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