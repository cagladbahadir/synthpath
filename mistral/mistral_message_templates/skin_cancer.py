# "skin": [0: "necrosis",
#          1: "skeletal muscle",
#          2: "eccrine sweat glands",
#          3: "vessels",
#          4: "elastosis",
#          5: "chondral tissue",
#          6: "hair follicle",
#          7: "epidermis",
#          8: "nerves",
#          9: "subcutis",
#          10: "dermis",
#          11: "sebaceous glands",
#          12: "squamous-cell carcinoma",
#          13: "melanoma in-situ",
#          14: "basal-cell carcinoma",
#          15: "naevus"
#          ],

def append_question_and_answer(message_dict, key, question, answers):
    for i in range(len(answers)):
        message_dict[key].append({"role": "assistant", "content": answers[i]})
        message_dict[key].append({"role": "user", "content": question})
    return message_dict
def message_skincancer():
    message_dict = {}
    # Necrosis
    message_dict[0] = [
    {"role": "user", "content": "Can you generate a single sentence of less than 15 words describing a pathology image that shows necrotic tissue in skin?"}]

    question = "Can you generate another sentence of less than 15 words describing a pathology image that shows necrotic tissue in skin?"
    answers = ["This is an image of necrosis in the skin tissue.",
               "This H&E stained tile of skin shows necrosis.",
               "Dead cells in the skin sample form a big necrotic patch.",
               "The biopsy of the skin reveals necrotic tissue."]

    message_dict = append_question_and_answer(message_dict, 0, question, answers)

    # Skeletal muscle
    message_dict[1] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 15 words describing a pathology image that shows skeletal muscle from a skin biopsy?"}]

    question = "Can you generate another sentence of less than 15 words describing a pathology image that shows skeletal muscle from a skin biopsy?"
    answers = ["This is an image of skeletal muscle taken from skin biopsy.",
               "This H&E stained tile shows skeletal muscle.",
               "The specimen taken from skin appears as skeletal muscle.",
               "The biopsy of the skin reveals skeletal muscle."]

    message_dict = append_question_and_answer(message_dict, 1, question, answers)

    # Eccrine sweat glands
    message_dict[2] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 15 words describing a pathology image that shows eccrine sweat glands from a skin biopsy?"}]

    question = "Can you generate another sentence of less than 15 words describing a pathology image that shows eccrine sweat glands from a skin biopsy?"
    answers = ["This is an image of eccrine sweat glands taken from skin biopsy.",
               "This H&E stained tile shows eccrine sweat glands.",
               "The specimen taken from skin appears as eccrine sweat glands.",
               "Eccrine sweat glands are important anatomical structures, as seen in the image."]

    message_dict = append_question_and_answer(message_dict, 2, question, answers)

    # Vessels
    message_dict[3] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 15 words describing a pathology image that shows vessels from a skin biopsy?"}]

    question = "Can you generate another sentence of less than 15 words describing a pathology image that shows vessels from a skin biopsy?"
    answers = ["This is an image of vessels seen from skin biopsy.",
               "This H&E stained tile shows vessels.",
               "The specimen taken from skin in focused on vessels.",
               "Vessels are important anatomical structures, as seen in the image."]

    message_dict = append_question_and_answer(message_dict, 3, question, answers)

    # Elastosis
    message_dict[4] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 15 words describing a pathology image that shows elastosis in a skin biopsy?"}]

    question = "Can you generate another sentence of less than 15 words describing a pathology image that shows elastosis in a skin biopsy?"
    answers = ["Elastosis is thickening of elastic fibers in the skin.",
               "This H&E stained tile shows elastosis condition in the skin.",
               "Degeneration of the elastic fibers is indicative of elastosis in the skin.",
               "This pathology slide shows elastosis in the skin."]

    message_dict = append_question_and_answer(message_dict, 4, question, answers)

    # chondral tissue
    message_dict[5] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 15 words describing a pathology image that shows chondral tissue in a skin biopsy?"}]

    question = "Can you generate another sentence of less than 15 words describing a pathology image that shows chondral tissue in a skin biopsy?"
    answers = ["The skin biopsy shows chondral tissue.",
               "This H&E stained tile is centered around chondral tissue.",
               "The specimen is acquired from skin and it reveals chondral tissue.",
               "This pathology slide is of chondral tissue."]

    message_dict = append_question_and_answer(message_dict, 5, question, answers)

    # Hair follicle
    message_dict[6] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 15 words describing a pathology image that shows hair follicle in a skin biopsy?"}]

    question = "Can you generate another sentence of less than 15 words describing a pathology image that shows hair follicle in a skin biopsy?"
    answers = ["The skin biopsy shows hair follicle.",
               "This H&E stained tile is of hair follicles.",
               "The specimen is acquired from skin and it reveals healthy hair follicles.",
               "Hair follicles can be clearly seen under the microscopic image."]

    message_dict = append_question_and_answer(message_dict, 6, question, answers)

    # Epidermis
    message_dict[7] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 15 words describing a pathology image that shows epidermis in a skin biopsy?"}]

    question = "Can you generate another sentence of less than 15 words describing a pathology image that shows epidermis in a skin biopsy?"
    answers = ["The epidermis is the top layer of the skin.",
               "The epidermis is seen in this pathology specimen taken from the skin.",
               "The H&E stained image highlights epidermis in the skin.",
               "Biopsy of the skin is taken from the epidermis."]

    message_dict = append_question_and_answer(message_dict, 7, question, answers)

    # nerves
    message_dict[8] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 15 words describing a pathology image that shows nerves in a skin biopsy?"}]

    question = "Can you generate another sentence of less than 15 words describing a pathology image that shows nerves in a skin biopsy?"
    answers = ["The biopsy of the skin shows nerves.",
               "Nerves are clearly visible in the microscopic image of the skin.",
               "The pathology specimen shows nerves.",
               "Nerves are apparent in the skin sample."]

    message_dict = append_question_and_answer(message_dict, 8, question, answers)

    # subcutis
    message_dict[9] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 15 words describing a pathology image that shows subcutis in a skin biopsy?"}]

    question = "Can you generate another sentence of less than 15 words describing a pathology image that shows subcutis in a skin biopsy?"
    answers = ["Subcutis tissue is the deepest layer of your skin.",
               "The pathology image shows subcutic tissue.",
               "The skin biopsy reveals subcutis tissue",
               "The H&E stained tile shows the subcutis in the skin."]

    message_dict = append_question_and_answer(message_dict, 9, question, answers)

    # dermis
    message_dict[10] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 15 words describing a pathology image that shows dermis in a skin biopsy?"}]

    question = "Can you generate another sentence of less than 15 words describing a pathology image that shows dermis in a skin biopsy?"
    answers = ["Dermis is the inner layer of the two main layers of the skin.",
               "The pathology image shows dermis.",
               "Dermis is apparent in the skin biopsy.",
               "The H&E stained tile is from the dermis."]

    message_dict = append_question_and_answer(message_dict, 10, question, answers)

    # sebaceous  glands
    message_dict[11] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 15 words describing a pathology image that shows sebaceous glands in a skin biopsy?"}]

    question = "Can you generate another sentence of less than 15 words describing a pathology image that shows sebaceous glands in a skin biopsy?"
    answers = ["Sebaceous glands are microscopic glands that secrete sebum.",
               "Sebaceous glands are seen in the H&3 stained tile.",
               "The pathology image is from sebaceous glands in the skin.",
               "Skin biopsy reveals healthy sebaceous glands."]

    message_dict = append_question_and_answer(message_dict, 11, question, answers)

    # squamous cell carcinoma
    message_dict[12] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 15 words describing a pathology image that shows squamous cell carcinoma in a skin biopsy?"}]

    question = "Can you generate another sentence of less than 15 words describing a pathology image that shows squamous cell carcinoma in a skin biopsy?"
    answers = ["The skin biopsy is diagnosed as squamous cell carcinoma.",
               "Squamous cell carcinoma is the apparent diagnosis from the pathology specimen.",
               "H&E stained tile shows squamous cell carcinoma.",
               "Squamous cell carcinoma of the skin is a type of cancer."]

    message_dict = append_question_and_answer(message_dict, 12, question, answers)

    # melanoma in situ
    message_dict[13] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 15 words describing a pathology image that shows melanoma in situ in a skin biopsy?"}]

    question = "Can you generate another sentence of less than 15 words describing a pathology image that shows melanoma in situ in a skin biopsy?"
    answers = ["Melanoma in situ is also called stage 0 melanoma.",
               "The skin biopsy is diagnosed as melanoma in situ.",
               "The pathology tile shows melanoma in situ in the skin.",
               "The abnormality in the microscopic image is melanoma in situ."]

    message_dict = append_question_and_answer(message_dict, 13, question, answers)

    # basal cell carcinoma
    message_dict[14] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 15 words describing a pathology image that shows basal cell carcinoma in a skin biopsy?"}]

    question = "Can you generate another sentence of less than 15 words describing a pathology image that shows basal cell carcinoma in a skin biopsy?"
    answers = ["Basal cell carcinoma is a type of skin cancer.",
               "Basal cell carcinoma is the diagnosis.",
               "Skin biopsy reveals basal cell carcinoma.",
               "The pathology tile shows basal cell carcinoma."]

    message_dict = append_question_and_answer(message_dict, 14, question, answers)

    # naevus
    message_dict[15] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 15 words describing a pathology image that shows naevus in a skin biopsy?"}]

    question = "Can you generate another sentence of less than 15 words describing a pathology image that shows naevus in a skin biopsy?"
    answers = ["The H&E stained tile shows naevus in a skin biopsy.",
               "The naevus is a birthmark or mole in the skin.",
               "The pathology tile shows naevus.",
               "The naevus is seen in the specimen from the skin."]

    message_dict = append_question_and_answer(message_dict, 15, question, answers)
    return message_dict