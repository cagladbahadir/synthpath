# "skin_tumor": [
#     "squamous-cell carcinoma",
#     "melanoma in-situ",
#     "basal-cell carcinoma",
#     "naevus"
# ]

def append_question_and_answer(message_dict, key, question, answers):
    for i in range(len(answers)):
        message_dict[key].append({"role": "assistant", "content": answers[i]})
        message_dict[key].append({"role": "user", "content": question})
    return message_dict
def message_skintumor():
    message_dict = {}

    # squamous cell carcinoma
    message_dict[0] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 8 words describing a pathology image that shows squamous cell carcinoma in a skin biopsy?"}]

    question = "Can you generate another sentence of less than 8 words describing a pathology image that shows squamous cell carcinoma in a skin biopsy?"
    answers = ["Skin diagnosed as squamous cell carcinoma.",
               "Squamous cell carcinoma revealed in biopsy.",
               "H&E stained tile shows squamous cell carcinoma.",
               "Squamous cell carcinoma is skin cancer."]

    message_dict = append_question_and_answer(message_dict, 0, question, answers)

    # melanoma in situ
    message_dict[1] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 8 words describing a pathology image that shows melanoma in situ in a skin biopsy?"}]

    question = "Can you generate another sentence of less than 8 words describing a pathology image that shows melanoma in situ in a skin biopsy?"
    answers = ["Melanoma in situ is also called stage 0 melanoma.",
               "Skin biopsy is diagnosed as melanoma in situ.",
               "Pathology tile shows melanoma in situ in the skin.",
               "Abnormality in microscopic image is melanoma in situ."]

    message_dict = append_question_and_answer(message_dict, 1, question, answers)

    # basal cell carcinoma
    message_dict[2] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 8 describing a pathology image that shows basal cell carcinoma in a skin biopsy?"}]

    question = "Can you generate another sentence of less than 8 words describing a pathology image that shows basal cell carcinoma in a skin biopsy?"
    answers = ["Basal cell carcinoma is a type of skin cancer.",
               "Basal cell carcinoma is the diagnosis.",
               "Skin biopsy reveals basal cell carcinoma.",
               "Pathology tile shows basal cell carcinoma."]

    message_dict = append_question_and_answer(message_dict, 2, question, answers)

    # naevus
    message_dict[3] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 8 words describing a pathology image that shows naevus in a skin biopsy?"}]

    question = "Can you generate another sentence of less than 8 words describing a pathology image that shows naevus in a skin biopsy?"
    answers = ["H&E stained tile shows naevus in a skin biopsy.",
               "Naevus is a birthmark or mole in skin.",
               "Pathology tile shows naevus.",
               "Naevus seen in the specimen from skin."]

    message_dict = append_question_and_answer(message_dict, 3, question, answers)
    return message_dict