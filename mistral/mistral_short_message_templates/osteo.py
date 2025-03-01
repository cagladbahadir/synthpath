# "osteo": ["non-tumor",
#           "non-viable necrotic osteosarcoma tumor",
#           "viable osteosarcoma tumor"
#           ],


def append_question_and_answer(message_dict, key, question, answers):
    for i in range(len(answers)):
        message_dict[key].append({"role": "assistant", "content": answers[i]})
        message_dict[key].append({"role": "user", "content": question})
    return message_dict
def message_osteo():
    message_dict = {}

    # non-tumor
    message_dict[0] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 8 words describing a pathology image that shows normal bone tissue?"}]

    question = "Can you generate another sentence of less than 15 words describing a pathology image that shows normal bone tissue?"

    answers = ["The sample appears normal and non-tumorous.",
               "The H&E stained tile reveals normal bone structure.",
               "The biopsy does not reveal tumor.",
               "This is a non-tumor area in the bone"]

    message_dict = append_question_and_answer(message_dict, 0, question, answers)

    # non-viable necrotic osteosarcoma tumor
    message_dict[1] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 15 words describing a pathology image that shows non-viable necrotic osteosarcoma tumor?"}]

    question = "Can you generate another sentence of less than 15 words describing a pathology image that shows non-viable necrotic osteosarcoma tumor?"
    answers = ["The sample is diagnosed as non viable necrotic osteosarcoma tumor.",
               "The cells are dead in the osteosarcoma tumor.",
               "Necrosis makes the osteosarcoma tumor non-viable.",
               "The biopsy is from a non viable area where osteosarcoma tumor has necrosis."]

    message_dict = append_question_and_answer(message_dict, 1, question, answers)

    # viable osteosarcoma tumor
    message_dict[2] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 15 words describing a pathology image that shows viable osteosarcoma tumor?"}]

    question = "Can you generate another sentence of less than 15 words describing a pathology image that shows viable necrotic osteosarcoma tumor?"
    answers = ["The pathology slide shows an active osteosarcoma tumor.",
               "The tumor is well fed and is indicative of osteosarcoma.",
               "The H&E slide is from a viable osteosarcoma tumor.",
               "This image shows that the tumor is osteosarcoma and it's viable."]

    message_dict = append_question_and_answer(message_dict, 2, question, answers)

    return message_dict