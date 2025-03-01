# {
#     "pcam": [
#         "lymph node",
#         "lymph node containing metastatic tumor tissue"
#     ],

def append_question_and_answer(message_dict, key, question, answers):
    for i in range(len(answers)):
        message_dict[key].append({"role": "assistant", "content": answers[i]})
        message_dict[key].append({"role": "user", "content": question})
    return message_dict
def message_pcam():
    message_dict = {}

    # lymph node
    message_dict[0] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 8 words describing a pathology image that shows normal lymph node?"}]

    question = "Can you generate another sentence of less than 8 words describing a pathology image that shows normal lymph node?"

    answers = ["The lymph biopsy is normal.",
               "The pathology image shows normal lymph node.",
               "H&E stained tile is from a healthy lymph node.",
               "Healthy lymph node is observed under the microscope."]

    message_dict = append_question_and_answer(message_dict, 0, question, answers)

    # lymph node containing metastatic tumor tissue
    message_dict[1] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 8 words describing a pathology image that shows lymph node containing metastatic tumor tissue?"}]

    question = "Can you generate another sentence of less than 8 words describing a pathology image that shows lymph node containing metastatic tumor tissue?"
    answers = ["The lymph node biopsy reveals metastatic tumor tissue.",
               "The metastatic tumor tissue if seen under the microscopic image of the lymph node.",
               "The H&E stained tile shows lymph node containing metastatic tumor tissue.",
               "Lymph node has metastatic tumor tissue."]

    message_dict = append_question_and_answer(message_dict, 1, question, answers)


    return message_dict