import torch
import torch.optim as optim
import torch.nn as nn
import numpy as np
import time
def logit_generate(x1, x2, logit_scale):
    x1 = x1 / x1.norm(dim=-1, keepdim=True)
    x2 = x2 / x2.norm(dim=-1, keepdim=True)

    # cosine similarity as logits
    logits_per_x1 = logit_scale * x1 @ x2.t()
    logits_per_x2 = logit_scale * x2 @ x1.t()

    return logits_per_x1, logits_per_x2

def logit_generate3d(x1, x2, logit_scale):
    x1 = x1 / x1.norm(dim=-1, keepdim=True)
    x2 = x2 / x2.norm(dim=-1, keepdim=True)

    logits_per_x1 = torch.bmm(logit_scale * x1, x2.permute(0,2,1))
    logits_per_x2 = torch.bmm(logit_scale * x2, x1.permute(0,2,1))
    return logits_per_x1, logits_per_x2

class TextCLIP(nn.Module):
    def __init__(self, model, model_name = ''):
        super(TextCLIP, self).__init__()
        self.model = model
        self.model_name = model_name

    def forward(self, text):
        if self.model.__class__.__name__ == 'CLIP':
            return self.model.encode_text(text)
        if self.model_name == 'conch':
            return self.model.encode_text(text)
        return self.model.get_text_features(text)


class ImageCLIP(nn.Module):
    def __init__(self, model, model_name = ''):
        super(ImageCLIP, self).__init__()
        self.model = model
        self.model_name = model_name

    def forward(self, image):
        if self.model.__class__.__name__ == 'CLIP':
            return self.model.encode_image(image)
        if self.model_name == 'conch':
            return self.model.encode_image(image)
        return self.model.get_image_features(image)

def model_save(epoch, model, optimizer, total_loss, save_dir_model, step):
    torch.save({
        'epoch': epoch,
        'model_state_dict': model.state_dict(),
        'optimizer_state_dict': optimizer.state_dict(),
        'loss': total_loss,
    }, save_dir_model + "/weights/model_checkpoint_step" + str(step) + ".pt")

def optimizer_parameters(model, learning_rate, weight_decay,scheduler, train_loader_size, optim_name):
    if optim_name == "AdamW":
        optimizer = optim.AdamW(model.parameters(), lr=float(learning_rate))
    elif optim_name == "Adam":
        optimizer = optim.Adam(model.parameters(), lr=float(learning_rate), betas=(0.9, 0.98), eps=1e-6,
                               weight_decay=float(weight_decay))
    elif optim_name == "SGD":
        optimizer = optim.SGD(model.parameters(), lr=float(learning_rate))

    if scheduler == 'cosine':
        scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, train_loader_size * 10)
    elif scheduler == 'warmup':
        scheduler1 = optim.lr_scheduler.CosineAnnealingWarmRestarts(optimizer, 10)
        scheduler2 = optim.lr_scheduler.CosineAnnealingLR(optimizer, train_loader_size * 10)
        scheduler = optim.lr_scheduler.SequentialLR(optimizer, schedulers=[scheduler1, scheduler2], milestones=[2])
    return optimizer, scheduler

def validation_print(step = None,
                     t0 = None,
                     validation_loss = None):
    print('At step:', step, ', ', np.around((time.time() - t0) / 60, decimals=2),
          ' minutes per 100 steps. Validation loss is: ', np.around(validation_loss, decimals=2),
          '%.')

def forward_pass(model_name = '',
                 model_image = None,
                 batch = None,
                 model_text = None,
                 model = None,
                 loss_img = None,
                 loss_txt = None,
                 device = None,
                 lambda_context = None,
                 beta = 1,
                 alpha = 1,

                 norm_context=1,
                 norm_image=1
    ):
    if 'context' not in model_name:
        return forward_pass_synth_net(model_name = model_name,
                 batch = batch,
                 model_text = model_text,
                 model_image = model_image,
                 model = model,
                 loss_img = loss_img,
                 loss_txt = loss_txt,
                 device = device,
                 lambda_context = lambda_context,
                 beta = beta,
                 alpha = alpha)
    elif 'context' in model_name:
        return forward_pass_synth_net_context(model_name = model_name,
                 batch = batch,
                 model_text = model_text,
                 model = model,
                 loss_img = loss_img,
                 loss_txt = loss_txt,
                 device = device,
                 lambda_context = lambda_context,
                 beta = beta,
                 alpha = alpha,

                  norm_context=norm_context,
                  norm_image=norm_image
                                              )

def forward_pass_synth_net_context (model_name = '',
                 model_image = None,
                 batch = None,
                 model_text = None,
                 model = None,
                 loss_img = None,
                 loss_txt = None,
                 device = None,
                 lambda_context = None,
                 beta = 1,
                 alpha = 1,

                norm_context=1,
                norm_image=1
                                    ):
    image_tensor, text_representation_cell, text_representation_organ, text_representation_disease = batch
    image_tensor = image_tensor.to(device)
    text_representation_cell = text_representation_cell.to(device)
    text_representation_organ = text_representation_organ.to(device)
    text_representation_disease = text_representation_disease.to(device)
    context = model(torch.tensor([0, 1, 2]).to(device))
    if norm_context == 'norm':
        context = context / context.norm(dim=-1, keepdim=True)
    if norm_context == 'norm':
        image_tensor = image_tensor / image_tensor.norm(dim=-1, keepdim=True)
    ground_truth = torch.arange(len(image_tensor), dtype=torch.long, device=device)

    logits_per_image, logits_per_text = logit_generate(image_tensor * context[0], text_representation_cell, 1)
    loss_cell = (loss_img(logits_per_image, ground_truth) + loss_txt(logits_per_text, ground_truth)) / 2

    logits_per_image, logits_per_text = logit_generate(image_tensor * context[1], text_representation_organ, 1)
    loss_organ = (loss_img(logits_per_image, ground_truth) + loss_txt(logits_per_text, ground_truth)) / 2

    logits_per_image, logits_per_text = logit_generate(image_tensor * context[2], text_representation_disease, 1)
    loss_disease = (loss_img(logits_per_image, ground_truth) + loss_txt(logits_per_text, ground_truth)) / 2

    loss = (1/3)* (loss_cell +  loss_organ + loss_disease)
    return logits_per_image, logits_per_text, ground_truth, loss
def forward_pass_synth_net(model_name = '',
                 model_image = None,
                 batch = None,
                 model_text = None,
                 model = None,
                 loss_img = None,
                 loss_txt = None,
                 device = None,
                 lambda_context = None,
                 beta = 1,
                 alpha = 1):
    times = [time.time()]

    print('Load data')
    image_tensor, text_tokens, text_tokens_cell, text_tokens_organ, text_tokens_disease = batch
    times.append(time.time())
    print(times[-1] - times[-2])

    print('Get features')
    image_features = model_image(image_tensor)
    text_features = model_text(text_tokens)
    logit_scale = model.logit_scale.exp()

    logits_per_image, logits_per_text = logit_generate(image_features, text_features, logit_scale)
    ground_truth = torch.arange(len(image_features), dtype=torch.long, device=device)
    loss = (loss_img(logits_per_image, ground_truth) + loss_txt(logits_per_text, ground_truth)) / 2

    return logits_per_image, logits_per_text, ground_truth, loss