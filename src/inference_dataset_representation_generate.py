from model_and_processor_load import image_representation_gather, model_select
from importer import *
from dataloader.mhist import mhist_loader
from dataloader.bach import bach_loader
from dataloader.lc_colon import lc_colon_loader
from dataloader.lc_lung import lc_lung_loader
from dataloader.renal_cell import renal_cell_loader
from dataloader.skin_tumor import skin_tumor_loader
from dataloader.skin_cancer import skin_cancer_loader
from dataloader.sicap import sicap_loader
from dataloader.crc import crc_loader
from dataloader.databiox import databiox_loader
from dataloader.pcam import camelyon_loader
from dataloader.pannuke_organ import pannuke_organ_loader
from dataloader.pannuke import pannuke_loader
from dataloader.ocelot_cell import ocelot_cell_loader
from dataloader.ocelot_organ import ocelot_organ_loader
import argparse

# Select dataset, model and model subtype
def parser_func():
    ## Training time
    parser = argparse.ArgumentParser()
    parser.add_argument("--fixed_embedding", default = 'quilt')
    parser.add_argument("--dataset", default='pannuke_cell')
    parser.add_argument("--subtype", default='B-32')
    parser.add_argument("--lora_layers", default='all')
    parser.add_argument("--lora_rank", default=8)
    parser.add_argument("--lora_alpha", default = 8)
    parser.add_argument("--lora_bias", default="none")
    parser.add_argument("--lora_dropout", default=0.05)
    parser.add_argument("--context_lambda", default=0.5)
    parser.add_argument("--rewrite_count", default=1)
    return parser

# Saving image reprsentations
def savefunc(savepath, test_features, images, labels, label_dict, args):

    savepath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', savepath + "/"))
    if not os.path.isdir(savepath): os.makedirs(savepath)
    torch.save(test_features, savepath + '/test_image_features.pt')
    torch.save(images, savepath + '/test_images.pt')
    torch.save(labels, savepath + '/labels.pt')
    torch.save(label_dict, savepath + '/label_dict.pt')
    with open(savepath + '/label_dict.pickle', 'wb') as handle:
        pickle.dump(label_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

def inference_on_dataset(args):
    fixed_embedding = args.fixed_embedding
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    frozen_model, preprocess_frozen_model = model_select('frozen', fixed_embedding, device, args.subtype, args)
    frozen_model = frozen_model.to(device)

    subtype = args.subtype
    subtype =  subtype.replace('/','_')
    context_text = '_context' if float(args.context_lambda) > 0 else ''

    dataset_dict = {'BACH': 'bach',
                    'LC_Lung': 'lc_lung',
                    'LC_Colon': 'lc_colon',
                     'MHIST':'mhist',
                    'Skin_cancer': 'skin_cancer',
                    'Renal_cell': 'renal_cell',
                    'Skin_tumor': 'skin_tumor',
                    'CRC':'nck_crc',
                    'SICAP': 'sicap',
                    'Databiox': 'databiox',
                    'Camelyon': 'pcam',
                    'Pannuke_Organ':'pannuke_organ',
                    'Ocelot_Cell': 'ocelot_cell',
                    'Ocelot_Organ': 'ocelot_organ',
                    'Pannuke_Cell': 'pannuke_cell'
    }
    dataset = dataset_dict[args.dataset]
    print(dataset)
    if dataset == 'skin_cancer':
        print('skin cancer')
        label_dict = {0: "necrosis",
                 1: "skeletal muscle",
                 2: "eccrine sweat glands",
                 3: "vessels",
                 4: "elastosis",
                 5: "chondral tissue",
                 6: "hair follicle",
                 7: "epidermis",
                 8: "nerves",
                 9: "subcutis",
                 10: "dermis",
                 11: "sebaceous glands",
                 12: "squamous-cell carcinoma",
                 13: "melanoma in-situ",
                 14: "basal-cell carcinoma",
                 15: "naevus"}
        images, labels = skin_cancer_loader(preprocess_frozen_model)
        savepath = 'Embeddings/Skin_cancer/' + args.fixed_embedding +"/" + subtype + "/"
        test_features = image_representation_gather(images, frozen_model, fixed_embedding, device)
        savefunc(savepath, test_features, images, labels, label_dict, args)

    elif dataset == 'skin_tumor':
        # Skin tumor
        print('skin tumor')
        label_dict = {0: "squamous-cell carcinoma",
        1: "melanoma in-situ",
        2: "basal-cell carcinoma",
        3: "naevus"}

        images, labels = skin_tumor_loader(preprocess_frozen_model)
        savepath = 'Embeddings/Skin_tumor/'  + args.fixed_embedding  +"/"+ subtype + "/"
        test_features = image_representation_gather(images, frozen_model, fixed_embedding, device)
        savefunc(savepath, test_features, images, labels, label_dict, args)

    elif dataset == 'renal_cell':
        print('renal cell')
        label_dict = {0: "red blood cells",
                      1: "renal cancer",
                      2: "normal renal tissue",
                      3: "torn adipose necrotic tissue",
                      4: "muscle fibrous stroma blood vessels"}
        images, labels = renal_cell_loader(preprocess_frozen_model)
        savepath = 'Embeddings/Renal_cell/' + args.fixed_embedding  +"/"+ subtype + "/"
        test_features = image_representation_gather(images, frozen_model, fixed_embedding, device)
        savefunc(savepath, test_features, images, labels, label_dict, args)

    elif dataset == 'lc_lung':
        print('lc lung')
        label_dict = {0: "lung adenocarcinoma",
                      1: "benign lung",
                      2: "lung squamous cell carcinoma"}
        images, labels = lc_lung_loader(preprocess_frozen_model)
        savepath = 'Embeddings/LC_Lung/' + args.fixed_embedding  +"/"+ subtype + "/"
        test_features = image_representation_gather(images, frozen_model, fixed_embedding, device)
        savefunc(savepath, test_features, images, labels, label_dict, args)

    elif dataset == 'lc_colon':
        # LC Colon
        label_dict = {0: "colon adenocarcinoma", 1: "benign colonic tissue", }
        images, labels = lc_colon_loader(preprocess_frozen_model)
        savepath = 'Embeddings/LC_Colon/' + args.fixed_embedding  +"/"+ subtype + "/"
        test_features = image_representation_gather(images, frozen_model, fixed_embedding, device)
        savefunc(savepath, test_features, images, labels, label_dict, args)

    elif dataset == 'bach':
        # BACH
        label_dict = {0: "breast non-malignant benign tissue",
                      1: "breast malignant in-situ carcinoma",
                      2: "breast malignant invasive carcinoma",
                      3: "normal breast tissue"}
        images, labels = bach_loader(preprocess_frozen_model)
        savepath = 'Embeddings/BACH/' + args.fixed_embedding  +"/"+ subtype + "/"
        test_features = image_representation_gather(images, frozen_model, fixed_embedding, device)
        savefunc(savepath, test_features, images, labels, label_dict, args)

    elif dataset == 'mhist':
        # MHIST
        label_dict = {0:"hyperplastic polyp", 1:"sessile serrated adenoma"}
        images, labels = mhist_loader(preprocess_frozen_model)
        savepath = 'Embeddings/MHIST/'  + args.fixed_embedding  +"/"+ subtype + "/"
        test_features = image_representation_gather(images, frozen_model, fixed_embedding, device)
        savefunc(savepath, test_features, images, labels, label_dict, args)

    elif dataset == 'sicap':
        label_dict = { 0: "benign glands",
                       1: "atrophic dense glands",
                       2: "cribriform ill-formed fused papillary patterns",
                       3: "isolated nest cells without lumen roseting patterns"}

        images, labels = sicap_loader(preprocess_frozen_model)
        savepath = 'Embeddings/SICAP/' + args.fixed_embedding  +"/"+ subtype + "/"
        test_features = image_representation_gather(images, frozen_model, fixed_embedding, device)
        savefunc(savepath, test_features, images, labels, label_dict, args)

    elif dataset == 'nck_crc':
        label_dict = { 0 :"adipose",
            1: "debris",
            2: "lymphocytes",
            3: "mucus",
            4: "smooth muscle",
            5: "normal colon mucosa",
            6: "cancer-associated stroma",
            7: "colorectal adenocarcinoma epithelium"
                       }
        images, labels = crc_loader(preprocess_frozen_model)
        savepath = 'Embeddings/CRC/'  + args.fixed_embedding  +"/"+ subtype + "/"
        test_features = image_representation_gather(images, frozen_model, fixed_embedding, device)
        savefunc(savepath, test_features, images, labels, label_dict, args)

    elif dataset == 'databiox':
        label_dict = { 0: "well differentiated bloom richardson grade one",
                   1: "moderately differentiated bloom richardson grade two",
                   2: "poorly differentiated grade three"}

        images, labels = databiox_loader(preprocess_frozen_model)
        savepath = 'Embeddings/Databiox/' + args.fixed_embedding  +"/"+ subtype + "/"
        test_features = image_representation_gather(images, frozen_model, fixed_embedding, device)
        savefunc(savepath, test_features, images, labels, label_dict, args)
    elif dataset == 'pcam':
        label_dict ={0:"lymph node", 1:"lymph node containing metastatic tumor tissue"}

        images, labels = camelyon_loader(preprocess_frozen_model)
        savepath = 'Embeddings/Camelyon/' + args.fixed_embedding  +"/"+ subtype + "/"
        test_features = image_representation_gather(images, frozen_model, fixed_embedding, device)
        savefunc(savepath, test_features, images, labels, label_dict, args)
    elif dataset == 'pannuke_organ':
        label_dict = {0: 'lung', 1: 'breast', 2: 'thyroid', 3: 'uterus', 4: 'skin', 5: 'esophagus', 6: 'liver', 7: 'testis',
         8: 'ovarian', 9: 'kidney', 10: 'prostate', 11: 'stomach', 12: 'adrenal gland', 13: 'bile duct', 14: 'cervix',
         15: 'headneck', 16: 'bladder', 17: 'pancreatic', 18: 'colon'}
        images, labels = pannuke_organ_loader(preprocess_frozen_model, label_dict)
        savepath = 'Embeddings/Pannuke_Organ/' + args.fixed_embedding  +"/"+ subtype + "/"
        test_features = image_representation_gather(images, frozen_model, fixed_embedding, device)
        savefunc(savepath, test_features, images, labels, label_dict, args)

    elif dataset == 'pannuke_cell':
        label_dict = {0: 'neoplastic cells',
                      1: 'inflammatory cells',
                      2: 'connective soft tissue cells',
                      3: 'dead cells',
                      4: 'epithelial cells'}
        images, labels = pannuke_loader(preprocess_frozen_model, label_dict)
        savepath = 'Embeddings/Pannuke_Cell/'  + args.fixed_embedding  +"/"+ subtype + "/"
        test_features = image_representation_gather(images, frozen_model, fixed_embedding, device)
        savefunc(savepath, test_features, images, labels, label_dict, args)

    elif dataset == 'ocelot_cell':
        label_dict = {0: 'normal cells',
                      1: 'tumor cells'}
        images, labels = ocelot_cell_loader(preprocess_frozen_model, label_dict)
        savepath = 'Embeddings/Ocelot_Cell/' + args.fixed_embedding  +"/"+ subtype + "/"
        test_features = image_representation_gather(images, frozen_model, fixed_embedding, device)
        savefunc(savepath, test_features, images, labels, label_dict, args)

    elif dataset == 'ocelot_organ':
        label_dict = {0: 'bladder',
                      1: 'endometrium',
                      2: 'head-and-neck',
                      3: 'kidney',
                      4: 'prostate',
                      5: 'stomach'}
        images, labels = ocelot_organ_loader(preprocess_frozen_model, label_dict)
        savepath = 'Embeddings/Ocelot_Organ/' + args.fixed_embedding  +"/"+ subtype + "/"
        test_features = image_representation_gather(images, frozen_model, fixed_embedding, device)
        savefunc(savepath, test_features, images, labels, label_dict, args)