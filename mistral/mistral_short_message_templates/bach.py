# "bach": ["breast non-malignant benign tissue",
#          "breast malignant in-situ carcinoma",
#          "breast malignant invasive carcinoma",
#          "breast normal breast tissue"],
def append_question_and_answer(message_dict, key, question, answers):
    for i in range(len(answers)):
        message_dict[key].append({"role": "assistant", "content": answers[i]})
        message_dict[key].append({"role": "user", "content": question})
    return message_dict
def message_bach():
    message_dict = {}

    # benign breast tissue
    message_dict[0] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 8 words describing a pathology image that shows non malignant benign breast tissue?"}]

    question = "Can you generate another sentence of less than 8 words describing a pathology image that shows non malignant benign breast tissue?"
    answers = ["The breast tissue appears benign.",
               "Pathology specimen is taken from benign breast tissue.",
               "H&E stained tile shows benign breast tissue.",
               "The microscopic image of the breast is benign."]

    message_dict = append_question_and_answer(message_dict, 0, question, answers)

    # breast malignant in-situ carcinoma
    message_dict[1] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 8 words describing a pathology image that shows malignant in situ carcinoma in breast tissue?"}]

    question = "Can you generate another sentence of less than 8 words describing a pathology image that shows malignant in situ carcinoma in breast tissue?"
    answers = ["The breast  is diagnosed with malignant in situ carcinoma.",
               "The breast cancer is contained and it's malignant.",
               "H&E stained breast reveals malignant in situ carcinoma.",
               "Breast sample shows malignant in situ carcinoma."]

    message_dict = append_question_and_answer(message_dict, 1, question, answers)

    # breast malignant invasive carcinoma
    message_dict[2] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 8 describing a pathology image that shows malignant invasive carcinoma in breast tissue?"}]

    question = "Can you generate another sentence of less than 8 words describing a pathology image that shows malignant invasive carcinoma in breast tissue?"
    answers = ["Breast diagnosis is malignant invasive carcinoma.",
               "This breast cancer is invasive and  malignant.",
               "H&E stained breast tile is malignant invasive carcinoma.",
               "The microscopic breast image reveals malignant invasive carcinoma."]

    message_dict = append_question_and_answer(message_dict, 2, question, answers)

    # breast normal breast tissue
    message_dict[3] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 8 words describing a pathology image that shows healthy and normal breast tissue?"}]

    question = "Can you generate another sentence of less than 8 words describing a pathology image that shows shows healthy and normal breast tissue?"
    answers = ["The breast tissue appears normal.",
               "Pathology specimen is taken from a healthy breast.",
               "H&E stained tile shows healthy breast tissue.",
               "The microscopic image of the breast is normal."]

    message_dict = append_question_and_answer(message_dict, 3, question, answers)
    return message_dict