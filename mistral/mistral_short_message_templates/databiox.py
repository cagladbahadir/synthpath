# "idc_grade": ["well differentiated bloom richardson grade one",
#               "moderately differentiated bloom richardson grade two",
#               "poorly differentiated grade three"
#               ],
# invasive ductal carcinoma
def append_question_and_answer(message_dict, key, question, answers):
    for i in range(len(answers)):
        message_dict[key].append({"role": "assistant", "content": answers[i]})
        message_dict[key].append({"role": "user", "content": question})
    return message_dict
def message_databiox():
    message_dict = {}

    # well differentiated bloom richardson grade one
    message_dict[0] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 8 words describing a pathology image that shows invasive ductal carcinoma of well differentiated bloom richardson grade one?"}]

    question = "Can you generate another sentence of less than 8 words describing a pathology image that shows invasive ductal carcinoma of well differentiated bloom richardson grade one?"

    answers = ["This image shows grade one IDC.",
               "The H&E slide image is grade one IDC.",
               "The cancer is IDC grade one.",
               "Breast surgery shows grade one IDC."]

    message_dict = append_question_and_answer(message_dict, 0, question, answers)

    # moderately differentiated bloom richardson grade two
    message_dict[1] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 8 words describing a pathology image that shows invasive ductal carcinoma of moderately differentiated bloom richardson grade two?"}]

    question = "Can you generate another sentence of less than 8 words describing a pathology image that shows invasive ductal carcinoma of moderately differentiated bloom richardson grade two?"

    answers = ["This image shows grade two IDC.",
               "The H&E slide image is grade two IDC.",
               "The cancer is IDC grade two.",
               "Breast surgery shows grade two IDC."]

    message_dict = append_question_and_answer(message_dict, 1, question, answers)

    # poorly differentiated grade three
    message_dict[2] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 8 words describing a pathology image that shows invasive ductal carcinoma of poorly differentiated grade three?"}]

    question = "Can you generate another sentence of less than 8 words describing a pathology image that shows invasive ductal carcinoma of poorly differentiated grade three?"

    answers = ["This image shows grade three IDC.",
               "The H&E slide image is grade three IDC.",
               "The cancer is IDC grade three.",
               "Breast surgery shows grade three IDC."]

    message_dict = append_question_and_answer(message_dict, 2, question, answers)

    return message_dict