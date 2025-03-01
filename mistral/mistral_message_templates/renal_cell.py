# "renal_cell": ["red blood cells",
#                "renal cancer",
#                "normal renal tissue",
#                "torn adipose necrotic tissue",
#                "muscle fibrous stroma blood vessels"
def append_question_and_answer(message_dict, key, question, answers):
    for i in range(len(answers)):
        message_dict[key].append({"role": "assistant", "content": answers[i]})
        message_dict[key].append({"role": "user", "content": question})
    return message_dict
def message_renal_cell():
    message_dict = {}

    # red blood cells
    message_dict[0] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 15 words describing a pathology image that has red blood cells?"}]

    question = "Can you generate another sentence of less than 15 words describing a pathology image that has red blood cells?"
    answers = ["The pathology image shows red blood cells.",
               "Blood cells appear red in the H&E stained image.",
               "Red blood cells are clustered together in the specimen.",
               "The biopsy is centered around the red blood cells."]

    message_dict = append_question_and_answer(message_dict, 0, question, answers)

    # renal cancer
    message_dict[1] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 15 words describing a pathology image that shows renal cancer?"}]

    question = "Can you generate another sentence of less than 15 words describing a pathology image that shows renal cancer?"
    answers = ["The pathology image shows renal cancer.",
               "The biopsy from the renal tissue revealed cancer.",
               "Abnormal cell growth in the specimen is indicative of cancer.",
               "Renal cancer is the first diagnosis that comes to mind, after seeing this microscopic image."]

    message_dict = append_question_and_answer(message_dict, 1, question, answers)

    # normal renal tissue
    message_dict[2] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 15 words describing a pathology image that shows normal renal tissue?"}]

    question = "Can you generate another sentence of less than 15 words describing a pathology image that shows normal renal tissue?"
    answers = ["The pathology image shows normal renal tissue.",
               "The renal tissue under the microscope appears normal.",
               "Renal biopsy did not show pathology and revealed normal tissue.",
               "A healthy and normal renal tissue looks like this in H&E stained slides."]

    message_dict = append_question_and_answer(message_dict, 2, question, answers)

    # torn adipose necrotic tissue
    message_dict[3] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 15 words describing a pathology image that shows torn adipose necrotic tissue?"}]

    question = "Can you generate another sentence of less than 15 words describing a pathology image that shows torn adipose necrotic tissue?"
    answers = ["The pathology image shows torn adipose necrotic tissue.",
               "The H&E stained section is from torn adipose necrotic tissue.",
               "In the torn adipose tissue there is apparent necrosis.",
               "The biopsy showed torn adipose necrotic tissue."]

    message_dict = append_question_and_answer(message_dict, 3, question, answers)

    #muscle fibrous stroma blood vessels
    message_dict[4] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 15 words describing a pathology image that shows muscle fibrous stroma blood vessels?"}]

    question = "Can you generate another sentence of less than 15 words describing a pathology image that shows muscle fibrous stroma blood vesselse?"
    answers = ["The pathology image shows muscle fibrous stroma blood vessels.",
               "The H&E stained section is from muscle fibrous stroma blood vessels.",
               "The biopsy shows muscle fibrous stroma blood vessels.",
               "Under the microscope muscle fibrous stroma blood vessels can be appreciated."]
    message_dict = append_question_and_answer(message_dict, 4, question, answers)

    return message_dict