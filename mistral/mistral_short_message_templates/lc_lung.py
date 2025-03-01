# "lc25000_lung": ["lung adenocarcinoma",
#                  "benign lung",
#                  "lung squamous cell carcinoma"

def message_lclung():
    message_dict = {}
    message_dict[0] = [
    {"role": "user", "content": "Can you generate a single sentence of less than 8 words describing a pathology image that has lung adenocarcinoma?"},
    {"role": "assistant", "content": "This image shows lung adenocarcinoma."},
    {"role": "user", "content": "Can you generate another sentence of less than 8 words describing a pathology image that has lung adenocarcinoma?"},
    {"role": "assistant", "content": "This H&E stained tile of lung is adenocarcinoma."},
    {"role": "user",
     "content": "Can you generate another sentence of less than 8 words describing a pathology image that has lung adenocarcinoma?"},
    {"role": "assistant", "content": "Adenocarcinoma if inferred from lung specimen."},
    {"role": "user",
     "content": "Can you generate another sentence of less than 8 words describing a pathology image that has lung adenocarcinoma?"},
    {"role": "assistant",
     "content": "The biopsy shows adenocarcinoma in the left lung."},
    {"role": "user",
     "content": "Can you generate another sentence of less than 8 words describing a pathology image that has lung adenocarcinoma?"},
]
    message_dict[1] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 8 words describing a pathology image that is benign lung tissue?"},
        {"role": "assistant", "content": "This image shows a benign lung tissue."},
        {"role": "user",
         "content": "Can you generate another sentence of less than 8 words describing a pathology image that is benign lung tissue?"},
        {"role": "assistant", "content": "This H&E stained tile of lung is benign."},
        {"role": "user",
         "content": "Can you generate another sentence of less than 8 words describing a pathology image that is benign lung tissue?"},
        {"role": "assistant",
         "content": "The benign lung tissue is apparent from the biopsy."},
        {"role": "user",
         "content": "Can you generate another sentence of less than 8 words describing a pathology image that is benign lung tissue?"},
        {"role": "assistant",
         "content": "This is an image of benign lung."},
        {"role": "user",
         "content": "Can you generate another sentence of less than 8 words describing a pathology image that is benign lung tissue?"},
    ]

    message_dict[2] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 8 words describing a pathology image that has lung squamous cell carcinoma?"},
        {"role": "assistant", "content": "This image shows a lung squamous cell carcinoma."},
        {"role": "user",
         "content": "Can you generate another sentence of less than 8 words describing a pathology image that has lung squamous cell carcinoma?"},
        {"role": "assistant", "content": "H&E stained lung tile reveals squamous cell carcinoma."},
        {"role": "user",
         "content": "Can you generate another sentence of less than 8 words describing a pathology image that has lung squamous cell carcinoma?"},
        {"role": "assistant",
         "content": "The biopsy revealed squamous cell carcinoma in lung."},
        {"role": "user",
         "content": "Can you generate another sentence of less than 8 words describing a pathology image that has lung squamous cell carcinoma?"},
        {"role": "assistant",
         "content": "Surgical resection of lung shows squamous cell carcinoma."},
        {"role": "user",
         "content": "Can you generate another sentence of less than 8 words describing a pathology image that has lung squamous cell carcinoma?"}
    ]
    return message_dict