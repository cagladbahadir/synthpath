from src.importer import *
# from dataloaders.dataloader import tcga_ids_retriever, report_reader, report_tokenizer, wsi_reader, wsi_reader_for_training, numpy_pairwise_combinations
# from trainer import tile_selector
# import clip
# import time
# from torch.utils.data import Dataset
# from torch.utils.data import DataLoader
# import random
# from models.plip.plip import PLIP
# from trainer import create_logits, TextCLIP, ImageCLIP, custom_collate
# from dataloaders.pannuke_loader import pannuke_train_and_validation
# from trainer import validation
# import pickle
# from trainer import model_select


# Mute warnings
warnings.simplefilter(action='ignore', category=RuntimeWarning)
torch.autograd.set_detect_anomaly(True)

# Set device for training
device = torch.device("cuda:" + str(torch.cuda.current_device()) if torch.cuda.is_available() else "cpu")


def set_parameters(args):
    """
    :param args:
    :return:
    """
    keys = list(vars(args).keys())

    save_dir_model = 'Training_Logs/Date_{dat}/Batch_{bch}/Time_'.format(
        dat=str(args.date),
        bch=str(args.batch_size)
        )

    time_ = int(time.time())
    if os.path.exists(save_dir_model):
        times = os.listdir(save_dir_model)
        while time_ in times:
            time_ = int(time.time())
    save_dir_model = save_dir_model + str(time_) + '/'
    print(save_dir_model)

    if not os.path.isdir(save_dir_model): os.makedirs(save_dir_model)
    np.savez(save_dir_model + "/History",
             train_loss=[],
             validation_loss = []
             )
    if not os.path.isdir(save_dir_model+'weights/'): os.makedirs(save_dir_model+'weights/')
    training_parameters = {}
    for key in keys:
        training_parameters[key] = getattr(args, key)
    with open(save_dir_model+'training_parameters.pickle', 'wb') as handle:
        pickle.dump(training_parameters, handle, protocol=pickle.HIGHEST_PROTOCOL)
    print(args)
    return save_dir_model


def parser_func():

    ## Training time

    parser = argparse.ArgumentParser()
    parser.add_argument("--ensemble", default = 1)
    parser.add_argument("--date", default = 'Jan12')
    parser.add_argument("--batch_size", type=int, default = 2)
    parser.add_argument("--location",default = 'local')
    parser.add_argument("--learning_rate", type=float, default = 1e-5)
    parser.add_argument("--optimizer", type=str, default = 'Adam')
    parser.add_argument("--scheduler", type=str, default='cosine')
    parser.add_argument("--loss_function", default = 'BCE')
    parser.add_argument("--fixed_embedding", default='quilt')
    parser.add_argument("--subtype", default='B-32')
    parser.add_argument("--weight_decay", default = 0.2)#0.2
    parser.add_argument("--lora_model", default = True)
    parser.add_argument("--context_specific_model", default = False)
    parser.add_argument("--training_mode", default = 'eval')
    parser.add_argument("--norm_context", default= 'not')
    parser.add_argument("--norm_image", default='not')

    ## Inference time
    parser.add_argument("--seed", default=10)
    parser.add_argument("--lora_layers", default='all')
    parser.add_argument("--lora_rank", default=8)
    parser.add_argument("--lora_alpha", default = 8)
    parser.add_argument("--lora_bias", default="none")
    parser.add_argument("--lora_dropout", default=0.05)
    parser.add_argument("--context_lambda", default = 0)
    return parser

global seeds

seeds = [5, 128, 670, 1023, 9845]


def set_seed(ensemble_id):
    seed = seeds[int(ensemble_id) - 1]
    torch.manual_seed(seed)  # Different for each ensemble
    random.seed(seed)
    np.random.seed(seed)

def initialize_train_parameters():
    step = 0
    train_loss = []
    validation_losses_all = []
    total_loss = 0
    t0 = time.time()
    t_step = time.time()
    return step, train_loss, validation_losses_all, total_loss, t0, t_step