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
         "content": "Can you generate a single sentence of less than 15 words describing a pathology image that shows invasive ductal carcinoma of well differentiated bloom richardson grade one?"}]

    question = "Can you generate another sentence of less than 15 words describing a pathology image that shows invasive ductal carcinoma of well differentiated bloom richardson grade one?"

    answers = ["This image shows invasive ductal carcinoma of well differentiated bloom richardson grade one.",
               "The H&E slide image is diagnosed with well differentiated bloom richardson grade one IDC.",
               "The cancer is well differentiated bloom richardson grade one.",
               "Breast surgery revealed well differentiated bloom richardson grade one IDC."]

    message_dict = append_question_and_answer(message_dict, 0, question, answers)

    # moderately differentiated bloom richardson grade two
    message_dict[1] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 15 words describing a pathology image that shows invasive ductal carcinoma of moderately differentiated bloom richardson grade two?"}]

    question = "Can you generate another sentence of less than 15 words describing a pathology image that shows invasive ductal carcinoma of moderately differentiated bloom richardson grade two?"

    answers = ["This image shows invasive ductal carcinoma of moderately differentiated bloom richardson grade two.",
               "The H&E slide image is diagnosed with moderately differentiated bloom richardson grade two IDC."
               "The cancer is moderately differentiated bloom richardson grade two.",
               "Breast surgery revealed moderately differentiated bloom richardson grade two IDC."]

    message_dict = append_question_and_answer(message_dict, 1, question, answers)

    # poorly differentiated grade three
    message_dict[2] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 15 words describing a pathology image that shows invasive ductal carcinoma of poorly differentiated grade three?"}]

    question = "Can you generate another sentence of less than 15 words describing a pathology image that shows invasive ductal carcinoma of poorly differentiated grade three?"

    answers = ["This image shows invasive ductal carcinoma of poorly differentiated grade three.",
               "The H&E slide image is diagnosed with poorly differentiated grade three IDC."
               "The cancer is poorly differentiated grade three.",
               "Breast surgery revealed poorly differentiated grade three IDC."]

    message_dict = append_question_and_answer(message_dict, 2, question, answers)

    return message_dict