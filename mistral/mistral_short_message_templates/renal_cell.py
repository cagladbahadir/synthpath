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
         "content": "Can you generate a single sentence of less than 8 words describing a pathology image that has red blood cells?"}]

    question = "Can you generate another sentence of less than 8 words describing a pathology image that has red blood cells?"
    answers = ["Pathology image shows red blood cells.",
               "Blood cells appear red in H&E image.",
               "Red blood cells are clustered",
               "Biopsy centers around the red blood cells."]

    message_dict = append_question_and_answer(message_dict, 0, question, answers)

    # renal cancer
    message_dict[1] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 8 words describing a pathology image that shows renal cancer?"}]

    question = "Can you generate another sentence of less than 8 words describing a pathology image that shows renal cancer?"
    answers = ["Pathology image shows renal cancer.",
               "Biopsy is from the cancerous renal tissue.",
               "Abnormal cell growth indicates renal cancer.",
               "Renal cancer is the first impression."]

    message_dict = append_question_and_answer(message_dict, 1, question, answers)

    # normal renal tissue
    message_dict[2] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 8 words describing a pathology image that shows normal renal tissue?"}]

    question = "Can you generate another sentence of less than 8 words describing a pathology image that shows normal renal tissue?"
    answers = ["Pathology image shows normal renal tissue.",
               "Renal tissue under the microscope appears normal.",
               "Renal biopsy revealed normal tissue.",
               "A healthy renal tissue looks like this."]

    message_dict = append_question_and_answer(message_dict, 2, question, answers)

    # torn adipose necrotic tissue
    message_dict[3] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 8 words describing a pathology image that shows torn adipose necrotic tissue?"}]

    question = "Can you generate another sentence of less than 8 words describing a pathology image that shows torn adipose necrotic tissue?"
    answers = ["Pathology image shows torn adipose necrotic tissue.",
               "H&E tile is from torn adipose necrotic tissue.",
               "Torn adipose tissue harbours necrosis.",
               "Biopsy showed torn adipose necrotic tissue."]

    message_dict = append_question_and_answer(message_dict, 3, question, answers)

    #muscle fibrous stroma blood vessels
    message_dict[4] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 8 words describing a pathology image that shows muscle fibrous stroma blood vessels?"}]

    question = "Can you generate another sentence of less than 8 words describing a pathology image that shows muscle fibrous stroma blood vesselse?"
    answers = ["Pathology image shows muscle fibrous stroma blood vessels.",
               "These are muscle fibrous stroma blood vessels.",
               "Biopsy shows muscle fibrous stroma blood vessels.",
               "Muscle fibrous stroma blood vessels seen via microscope."]
    message_dict = append_question_and_answer(message_dict, 4, question, answers)

    return message_dict