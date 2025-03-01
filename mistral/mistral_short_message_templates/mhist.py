# "mhist": ["hyperplastic polyp",
#           "sessile serrated adenoma"
#           ],


def append_question_and_answer(message_dict, key, question, answers):
    for i in range(len(answers)):
        message_dict[key].append({"role": "assistant", "content": answers[i]})
        message_dict[key].append({"role": "user", "content": question})
    return message_dict
def message_mhist():
    message_dict = {}

    # hyperplastic polyp
    message_dict[0] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 8 words describing a pathology image that shows hyperplastic polyp?"}]

    question = "Can you generate another sentence of less than 8 words describing a pathology image that shows hyperplastic polyp?"

    answers = ["The sample shows hyperplastic polyp.",
               "H&E stained tile is from hyperplastic polyp.",
               "The biopsy reveals hyperplastic polyp.",
               "Hyperplastic polyp can be seen in the tissue."]

    message_dict = append_question_and_answer(message_dict, 0, question, answers)

    # sessile serrated adenoma
    message_dict[1] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 8 words describing a pathology image that shows sessile serrated adenoma?"}]

    question = "Can you generate another sentence of less than 8 words describing a pathology image that shows sessile serrated adenomar?"
    answers = ["The sample diagnosis is sessile serrated adenoma.",
               "Sessile serrated polyps are a type of neoplastic polyp.",
               "Colorectal biopsy is diagnosed with sessile serrated adenoma.",
               "The H&E stained sample indicates sessile serrated adenoma."]

    message_dict = append_question_and_answer(message_dict, 1, question, answers)


    return message_dict