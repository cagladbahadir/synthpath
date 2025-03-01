import clip
import open_clip
import torch
import torch.nn as nn
from peft import LoraConfig, TaskType, get_peft_model
from transformers import CLIPProcessor, CLIPModel
from PIL import Image

import matplotlib.pyplot as plt
import numpy as np
import urllib
from scipy.ndimage import filters
from torch import nn
import urllib.request
import numpy as np
import torch
import torch.nn.functional as F
import os

def model_select(context_or_frozen, model_name, device, subtype, args):
    if model_name == 'clip':
        frozen_model, preprocess = clip.load( subtype, device=device, jit=False)
    elif model_name == 'quilt':
        frozen_model, preprocess, preprocess_val = open_clip.create_model_and_transforms(
                'hf-hub:wisdomik/QuiltNet-' + subtype)
        frozen_model = CLIPModel.from_pretrained('wisdomik/QuiltNet-' + subtype)
    elif model_name == 'synth_net':
        frozen_model, preprocess, preprocess_val = open_clip.create_model_and_transforms(
            'hf-hub:wisdomik/QuiltNet-' + subtype)
        model = CLIPModel.from_pretrained('wisdomik/QuiltNet-'+subtype)
        target_modules = []
        for name, layer in model.named_modules():
            if args.lora_layers == 'all':
                if isinstance(layer, torch.nn.Linear) or isinstance(layer, torch.nn.Conv1d):
                    target_modules.append(name)
        lora_config = LoraConfig(
            r=args.lora_rank,
            target_modules=target_modules,
            lora_alpha=args.lora_alpha,
            lora_dropout=args.lora_dropout,
            bias=args.lora_bias)
        frozen_model = get_peft_model(model, lora_config)

        weight_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'weights/'))
        checkpoint = torch.load(weight_path + '/synth_path_checkpoint.pt', map_location = device)
        pretrained_dict = checkpoint['model_state_dict']
        frozen_model.load_state_dict(pretrained_dict, strict = True)

    frozen_model.eval()
    return frozen_model, preprocess

def training_model_select(args, device):
    model_name = args.fixed_embedding

    if model_name == 'clip':
        model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
        processor = CLIPProcessor.from_pretrained('wisdomik/QuiltNet-B-32')
        model.eval()

    elif model_name == 'quilt':
        model = CLIPModel.from_pretrained('wisdomik/QuiltNet-' + args.subtype)
        processor = CLIPProcessor.from_pretrained('wisdomik/QuiltNet-' + args.subtype)
        tokenizer = open_clip.get_tokenizer('hf-hub:wisdomik/QuiltNet-' + args.subtype)
        target_modules = []
        for name, layer in model.named_modules():
            if args.lora_layers == 'all':
                if isinstance(layer, torch.nn.Linear) or isinstance(layer, torch.nn.Conv1d):
                    target_modules.append(name)
        lora_config = LoraConfig(
            r=args.lora_rank,
            target_modules=target_modules,
            lora_alpha=args.lora_alpha,
            lora_dropout=args.lora_dropout,
            bias=args.lora_bias)

        model = get_peft_model(model, lora_config)
        model.config.gradient_checkpointing = True
        model.eval()

    elif model_name == 'synth_net_context':
        model = nn.Embedding(num_embeddings = 3, embedding_dim = 512)
        torch.nn.init.ones_(model.weight)
        processor = []
        tokenizer = []
    return model, processor, tokenizer

class ImageCLIP(nn.Module):
    def __init__(self, model, model_type):
        super(ImageCLIP, self).__init__()
        self.model = model
        self.model_type = model_type

    def forward(self, image):
        if self.model_type == 'clip':
            return self.model.encode_image(image)
        if self.model_type == 'quilt' or self.model_type == 'synth_net':
            return self.model.get_image_features(image)

def image_representation_gather(tiles, frozen_model, model_type, device):
    model_image = ImageCLIP(frozen_model, model_type)
    image_features = []
    with (torch.no_grad()):
        for i in range(tiles.shape[0]):
            image_features.append(model_image(tiles[i:i + 1].to(device)).cpu())
    image_features = torch.vstack(image_features)
    return image_features

def tokenizer_select(model_name, processor):
    if model_name == 'quilt' or model_name == 'synth_net':
        tokenizer = open_clip.get_tokenizer('hf-hub:wisdomik/QuiltNet-B-32')
    elif model_name == 'clip':
        tokenizer = clip.tokenize
    return tokenizer

def tokenize_custom(text, tokenizer, model_type):
    cut = len(text)
    exception = True
    while exception:
        try:
            tokenized = tokenizer(text[0:cut])
            exception = False
        except:
            cut -= 10

    return tokenized