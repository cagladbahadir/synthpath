# "nck": ["adipose",
#         "debris",
#         "lymphocytes",
#         "mucus",
#         "smooth muscle",
#         "normal colon mucosa",
#         "cancer associated stroma",
#         "colorectal adenocarcinoma epithelium"
#         ],


def append_question_and_answer(message_dict, key, question, answers):
    for i in range(len(answers)):
        message_dict[key].append({"role": "assistant", "content": answers[i]})
        message_dict[key].append({"role": "user", "content": question})
    return message_dict
def message_nck_crc():
    message_dict = {}

    # adipose
    message_dict[0] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 15 words describing a pathology image that shows adipose tissue in the colon?"}]

    question = "Can you generate another sentence of less than 15 words describing a pathology image that shows adipose tissue in the colon?"

    answers = ["This image shows adipose tissue in the colon.",
               "The H&E stained tile is from the adipose tissue in the colorectal area.",
               "The biopsy is taken from the adipose tisue in the colon.",
               "Adipose tissue looks normal in the colon sample."]

    message_dict = append_question_and_answer(message_dict, 0, question, answers)

    # debris
    message_dict[1] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 15 words describing a pathology image that shows debris in the colon sample?"}]

    question = "Can you generate another sentence of less than 15 words describing a pathology image that shows debris in the colon sample?"

    answers = ["The image shows debris in the colon.",
               "The pathology sample from the colon shows debris.",
               "Debris affects the correct diagnosis of the colon sample.",
               "Debris can be seen in the H&E stained tile of the colon."]

    message_dict = append_question_and_answer(message_dict, 1, question, answers)

    # lymphocytes
    message_dict[2] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 15 words describing a pathology image that shows lymphocytes in the colon sample?"}]

    question = "Can you generate another sentence of less than 15 words describing a pathology image that shows lymphocytes in the colon sample?"

    answers = ["A lymphocyte is a type of white blood cell.",
               "Lymphocytes are seen under the microscopic image of the colon.",
               "The colorectal specimen reveals lymphocytes.",
               "The H&E stained image reveals lymphocytes in the colon sample."]

    message_dict = append_question_and_answer(message_dict, 2, question, answers)

    # mucus
    message_dict[3] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 15 words describing a pathology image that shows mucus in the colon sample?"}]

    question = "Can you generate another sentence of less than 15 words describing a pathology image that shows mucus in the colon sample?"

    answers = ["Mucus is clearly visible in the microscopic image of the colon.",
               "The H&E stained image of the colon shows mucus.",
               "Mucus in the colon is normal.",
               "Mucus is present in the microscopic image of the colorectal tissue."]

    message_dict = append_question_and_answer(message_dict, 3, question, answers)

    # smooth muscle
    message_dict[4] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 15 words describing a pathology image that shows smooth muscle in the colon sample?"}]

    question = "Can you generate another sentence of less than 15 words describing a pathology image that shows smooth muscle in the colon sample?"

    answers = ["This biopsy is taken from the smooth muscle in the colorectal area.",
               "Smooth muscle appearance is normal for colon.",
               "The pathology image is from the smooth muscle in the colon.",
               "Colorectal sample shows smooth muscle."]

    message_dict = append_question_and_answer(message_dict, 4, question, answers)

    # normal colon mucosa
    message_dict[5] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 15 words describing a pathology image that shows normal colon mucosa?"}]

    question = "Can you generate another sentence of less than 15 words describing a pathology image that shows normal colon mucosa?"

    answers = ["The sample is from normal colon mucosa.",
               "The H&E stained image shows normal colon mucosa.",
               "Normal colon mucosa would look like this under the microscope.",
               "The pathology specimen is from normal colon mucosa."]

    message_dict = append_question_and_answer(message_dict, 5, question, answers)

    # cancer associated stroma
    message_dict[6] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 15 words describing a pathology image that shows cancer associated stroma in the colon?"}]

    question = "Can you generate another sentence of less than 15 words describing a pathology image that shows cancer associated stroma in the colon?"

    answers = ["The colorectal biopsy was diagnosed with cancer associated stroma.",
               "Cancer associated stroma is the official diagnosis of the colon sample.",
               "Colorectal tissue showed cancer associated stroma.",
               "The pathology is cancer associated stroma."]

    message_dict = append_question_and_answer(message_dict, 6, question, answers)

    # colorectal adenocarcinoma epithelium
    message_dict[7] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 15 words describing a pathology image that shows colorectal adenocarcinoma epithelium?"}]

    question = "Can you generate another sentence of less than 15 words describing a pathology image that shows colorectal adenocarcinoma epithelium?"

    answers = ["This is the typical manifestation of the colorectal adenocarcinoma epithelium.",
               "The tile centers around colorectal adenocarcinoma epithelium.",
               "H&E stained colorectal sample shows colorectal adenocarcinoma epithelium.",
               "Colorectal adenocarcinoma epithelium is very visible."]


    message_dict = append_question_and_answer(message_dict, 7, question, answers)


    return message_dict