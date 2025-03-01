
def append_question_and_answer(message_dict, key, question, answers):
    for i in range(len(answers)):
        message_dict[key].append({"role": "assistant", "content": answers[i]})
        message_dict[key].append({"role": "user", "content": question})
    return message_dict


def message_ocelot_cell():
    label_dict = {0: 'normal cells',
                  1: 'tumor cells'}
    default_question = {"role": "user", "content": "Can you generate a single sentence of less than 8 words describing a pathology image that has [CELLS]?"}

    question = "Can you generate another sentence of less than 8 words describing a pathology image that has [CELLS]?"
    answers = ["In this image [CELLS] are clearly observed.",
               "An H&E stained slide contains [CELLS].",
               "The biopsy reveals a groups of [CELLS].",
               "Under the microscope, [CELLS] can be identified."]

    message_dict = {}
    for cell_key in label_dict.keys():
        cell = label_dict[cell_key]
        message_dict[cell_key] = [default_question.copy()]
        message_dict[cell_key][0]["content"] =  message_dict[cell_key][0]["content"].replace('[CELLS]', cell)
        message_dict = append_question_and_answer(message_dict, cell_key, question.replace('[CELLS]', cell), \
                                                  [answer.replace('[CELLS]', cell) for answer in answers])

    return message_dict