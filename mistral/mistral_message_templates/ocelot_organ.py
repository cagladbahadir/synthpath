
def append_question_and_answer(message_dict, key, question, answers):
    for i in range(len(answers)):
        message_dict[key].append({"role": "assistant", "content": answers[i]})
        message_dict[key].append({"role": "user", "content": question})
    return message_dict


def message_ocelot_organ():
    label_dict = {0: 'bladder',
                  1: 'endometrium',
                  2: 'head and neck',
                  3: 'kidney',
                  4: 'prostate',
                  5: 'stomach'}
    default_question = {"role": "user", "content": "Can you generate a single sentence of less than 15 words describing a pathology image from [ORGANHERE]?"}

    question = "Can you generate another sentence of less than 15 words describing a pathology image from [ORGANHERE]?"
    answers = ["This is an image originating from the [ORGANHERE].",
               "An H&E stained [ORGANHERE] sample is clearly seen under the microscope.",
               "This pathology image is from a [ORGANHERE] biopsy.",
               "The [ORGANHERE] tissue is observed."]

    message_dict = {}
    for organ_key in label_dict.keys():
        organ = label_dict[organ_key]
        message_dict[organ_key] = [default_question.copy()]
        message_dict[organ_key][0]["content"] =  message_dict[organ_key][0]["content"].replace('[ORGANHERE]', organ)
        message_dict = append_question_and_answer(message_dict, organ_key, question.replace('[ORGANHERE]', organ), \
                                                  [answer.replace('[ORGANHERE]', organ) for answer in answers])

    return message_dict