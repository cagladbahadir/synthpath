from model_and_processor_load import tokenizer_select, tokenize_custom
import numpy as np
from train_helper import logit_generate
import random
import torch

def zeroshot_classification(image_features = None,
                          class_labels = None,
                          prompts = None,
                          embedding_model = None,
                          model_logit = None,
                          model_name = None,
                          preprocess = None,
                          device = None,
                          prompt_embedding = None,
                          ):

    tokenizer = tokenizer_select(model_name, preprocess)
    class_embeddings = [0]*len(prompts.keys())
    embedding_with_keys = {}
    with torch.no_grad():
        if prompt_embedding != None:
            class_embeddings = prompt_embedding.to(device)
        else:
            for i in prompts.keys():
                class_embeddings[i] = embedding_model(tokenize_custom(prompts[i], tokenizer, model_name).to(device))
                embedding_with_keys[i] = class_embeddings[i] / class_embeddings[i].norm(dim=-1, keepdim=True)
            class_embeddings = torch.vstack(class_embeddings).detach()


        logit_scale = model_logit
        logits_per_image, logits_per_text = logit_generate(image_features.float().to(device) , class_embeddings.float().to(device),
                                                                      logit_scale)
        probs = logits_per_image.softmax(dim=-1).cpu().numpy()
        accuracy = np.mean(np.argmax(probs,axis=1)==np.array(class_labels.cpu().numpy()))

    return accuracy, probs, embedding_with_keys, logits_per_image

