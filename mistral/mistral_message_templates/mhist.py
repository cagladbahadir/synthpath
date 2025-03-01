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
         "content": "Can you generate a single sentence of less than 15 words describing a pathology image that shows hyperplastic polyp?"}]

    question = "Can you generate another sentence of less than 15 words describing a pathology image that shows hyperplastic polyp?"

    answers = ["The sample shows hyperplastic polyp.",
               "The H&E stained tile reveals noncancerous growth named hyperplastic polyp.",
               "The biopsy from the colorectal tissue reveals hyperplastic polyp.",
               "Hyperplastic polyp can be seen in the colorectal tissue."]

    message_dict = append_question_and_answer(message_dict, 0, question, answers)

    # sessile serrated adenoma
    message_dict[1] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 15 words describing a pathology image that shows sessile serrated adenoma?"}]

    question = "Can you generate another sentence of less than 15 words describing a pathology image that shows sessile serrated adenomar?"
    answers = ["The sample is diagnosed with sessile serrated adenoma.",
               "Sessile serrated polyps are a recently recognized type of neoplastic polyp.",
               "Colorectal biopsy is diagnosed with sessile serrated adenoma.",
               "The H&E stained sample is indicative of sessile serrated adenoma."]

    message_dict = append_question_and_answer(message_dict, 1, question, answers)


    return message_dict