    # "lc25000_colon": ["colon adenocarcinoma",
    #                   "benign colonic tissue"

def message_lccolon():
    message_dict = {}
    message_dict[0] = [
    {"role": "user", "content": "Can you generate a single sentence of less than 15 words describing a pathology image that has colon adenocarcinoma?"},
    {"role": "assistant", "content": "This image shows colon adenocarcinoma."},
    {"role": "user", "content": "Can you generate another sentence of less than 15 words describing a pathology image that has colon adenocarcinoma?"},
    {"role": "assistant", "content": "This H&E stained tile of colon is diagnosed with adenocarcinoma."},
    {"role": "user",
     "content": "Can you generate another sentence of less than 15 words describing a pathology image that has colon adenocarcinoma?"},
    {"role": "assistant", "content": "Adenocarcinoma can be inferred in the histopathology specimen from the colon."},
    {"role": "user",
     "content": "Can you generate another sentence of less than 15 words describing a pathology image that has colon adenocarcinoma?"},
    {"role": "assistant",
     "content": "The biopsy shows adenocarcinoma in the colon."},
    {"role": "user",
     "content": "Can you generate another sentence of less than 15 words describing a pathology image that has colon adenocarcinoma?"},
]

    message_dict[1] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 15 words describing a pathology image that shows benign colonic tissue?"},
        {"role": "assistant", "content": "This image shows benign colonic tissue."},
        {"role": "user",
         "content": "Can you generate another sentence of less than 15 words describing a pathology image that shows benign colonic tissue?"},
        {"role": "assistant", "content": "This H&E stained tile of the colon is benign."},
        {"role": "user",
         "content": "Can you generate another sentence of less than 15 words describing a pathology image that shows benign colonic tissue?"},
        {"role": "assistant",
         "content": "The histopathology specimen from the colon appears benign."},
        {"role": "user",
         "content": "Can you generate another sentence of less than 15 words describing a pathology image that shows benign colonic tissue?"},
        {"role": "assistant",
         "content": "The biopsy doesn't show abnormalities and the colon tissue appears benign."},
        {"role": "user",
         "content": "Can you generate another sentence of less than 15 words describing a pathology image that shows benign colonic tissue?"},
    ]
    return message_dict