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
    {"role": "user", "content": "Can you generate a single sentence of less than 8 words describing a pathology image that shows necrotic tissue in skin?"}]

    question = "Can you generate another sentence of less than 8 words describing a pathology image that shows necrotic tissue in skin?"
    answers = ["This is an image of necrosis in the skin tissue.",
               "This H&E stained tile of skin shows necrosis.",
               "Dead cells in skin sample form necrosis.",
               "The biopsy of the skin reveals necrotic tissue."]

    message_dict = append_question_and_answer(message_dict, 0, question, answers)

    # Skeletal muscle
    message_dict[1] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 8 words describing a pathology image that shows skeletal muscle from a skin biopsy?"}]

    question = "Can you generate another sentence of less than 8 words describing a pathology image that shows skeletal muscle from a skin biopsy?"
    answers = ["Image of skeletal muscle taken from skin biopsy.",
               "This H&E stained tile shows skeletal muscle.",
               "Specimen taken from skin appears as skeletal muscle.",
               "Biopsy of the skin reveals skeletal muscle."]

    message_dict = append_question_and_answer(message_dict, 1, question, answers)

    # Eccrine sweat glands
    message_dict[2] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 8 words describing a pathology image that shows eccrine sweat glands from a skin biopsy?"}]

    question = "Can you generate another sentence of less than 8 words describing a pathology image that shows eccrine sweat glands from a skin biopsy?"
    answers = ["Image of eccrine sweat glands from skin biopsy.",
               "H&E stained tile shows eccrine sweat glands.",
               "Specimen from skin appears as eccrine sweat glands.",
               "Eccrine sweat glands are in the skin."]

    message_dict = append_question_and_answer(message_dict, 2, question, answers)

    # Vessels
    message_dict[3] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 8 words describing a pathology image that shows vessels from a skin biopsy?"}]

    question = "Can you generate another sentence of less than 8 words describing a pathology image that shows vessels from a skin biopsy?"
    answers = ["Image of vessels seen from skin biopsy.",
               "This H&E stained tile shows vessels.",
               "The specimen taken from skin in focused on vessels.",
               "Vessels are anatomical structures in skin."]

    message_dict = append_question_and_answer(message_dict, 3, question, answers)

    # Elastosis
    message_dict[4] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 8 words describing a pathology image that shows elastosis in a skin biopsy?"}]

    question = "Can you generate another sentence of less than 8 words describing a pathology image that shows elastosis in a skin biopsy?"
    answers = ["Elastosis is thickening of elastic fibers in the skin.",
               "H&E stained tile shows elastosis in skin.",
               "Pathology indicative of elastosis in the skin.",
               "Pathology slide shows elastosis in the skin."]

    message_dict = append_question_and_answer(message_dict, 4, question, answers)

    # chondral tissue
    message_dict[5] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 8 words describing a pathology image that shows chondral tissue in a skin biopsy?"}]

    question = "Can you generate another sentence of less than 8 words describing a pathology image that shows chondral tissue in a skin biopsy?"
    answers = ["The skin biopsy shows chondral tissue.",
               "H&E stained tile is centered around chondral tissue.",
               "Specimen acquired from skin reveals chondral tissue.",
               "This pathology slide is of chondral tissue."]

    message_dict = append_question_and_answer(message_dict, 5, question, answers)

    # Hair follicle
    message_dict[6] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 8 words describing a pathology image that shows hair follicle in a skin biopsy?"}]

    question = "Can you generate another sentence of less than 8 words describing a pathology image that shows hair follicle in a skin biopsy?"
    answers = ["The skin biopsy shows hair follicle.",
               "This H&E stained tile is of hair follicles.",
               "Specimen shows healthy hair follicles.",
               "Hair follicles under the microscopic image."]

    message_dict = append_question_and_answer(message_dict, 6, question, answers)

    # Epidermis
    message_dict[7] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 8 words describing a pathology image that shows epidermis in a skin biopsy?"}]

    question = "Can you generate another sentence of less than 8 words describing a pathology image that shows epidermis in a skin biopsy?"
    answers = ["Epidermis is the top layer of skin.",
               "Epidermis is seen in this pathology specimen of skin.",
               "H&E stained image shows skin epidermis.",
               "Biopsy of skin is taken from the epidermis."]

    message_dict = append_question_and_answer(message_dict, 7, question, answers)

    # nerves
    message_dict[8] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 8 words describing a pathology image that shows nerves in a skin biopsy?"}]

    question = "Can you generate another sentence of less than 8 words describing a pathology image that shows nerves in a skin biopsy?"
    answers = ["The biopsy of the skin shows nerves.",
               "Nerves visible in microscopic image of skin.",
               "The pathology specimen shows nerves.",
               "Nerves are apparent in the skin sample."]

    message_dict = append_question_and_answer(message_dict, 8, question, answers)

    # subcutis
    message_dict[9] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 8 words describing a pathology image that shows subcutis in a skin biopsy?"}]

    question = "Can you generate another sentence of less than 8 words describing a pathology image that shows subcutis in a skin biopsy?"
    answers = ["Subcutis tissue is deepest layer of skin.",
               "The pathology image shows subcutic tissue.",
               "skin biopsy reveals subcutis tissue",
               "H&E stained tile shows subcutis in skin."]

    message_dict = append_question_and_answer(message_dict, 9, question, answers)

    # dermis
    message_dict[10] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 8 words describing a pathology image that shows dermis in a skin biopsy?"}]

    question = "Can you generate another sentence of less than 8 words describing a pathology image that shows dermis in a skin biopsy?"
    answers = ["Dermis is inner layer of skin.",
               "The pathology image shows dermis.",
               "Dermis is apparent in the skin biopsy.",
               "The H&E stained tile is from the dermis."]

    message_dict = append_question_and_answer(message_dict, 10, question, answers)

    # sebaceous  glands
    message_dict[11] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 8 words describing a pathology image that shows sebaceous glands in a skin biopsy?"}]

    question = "Can you generate another sentence of less than 8 words describing a pathology image that shows sebaceous glands in a skin biopsy?"
    answers = ["Sebaceous glands secrete sebum.",
               "Sebaceous glands seen in H&3 stained tile.",
               "Pathology image from sebaceous glands in the skin.",
               "Skin biopsy reveals healthy sebaceous glands."]

    message_dict = append_question_and_answer(message_dict, 11, question, answers)

    # squamous cell carcinoma
    message_dict[12] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 8 words describing a pathology image that shows squamous cell carcinoma in a skin biopsy?"}]

    question = "Can you generate another sentence of less than 8 words describing a pathology image that shows squamous cell carcinoma in a skin biopsy?"
    answers = ["Skin biopsy diagnosed with squamous cell carcinoma.",
               "Squamous cell carcinoma is apparent.",
               "H&E stained tile shows squamous cell carcinoma.",
               "Squamous cell carcinoma is skin cancer."]

    message_dict = append_question_and_answer(message_dict, 12, question, answers)

    # melanoma in situ
    message_dict[13] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 8 words describing a pathology image that shows melanoma in situ in a skin biopsy?"}]

    question = "Can you generate another sentence of less than 8 words describing a pathology image that shows melanoma in situ in a skin biopsy?"
    answers = ["Melanoma in situ is also called stage 0 melanoma.",
               "Skin biopsy is diagnosed as melanoma in situ.",
               "Pathology tile shows melanoma in situ in skin.",
               "Abnormality under microscope is melanoma in situ."]

    message_dict = append_question_and_answer(message_dict, 13, question, answers)

    # basal cell carcinoma
    message_dict[14] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 8 words describing a pathology image that shows basal cell carcinoma in a skin biopsy?"}]

    question = "Can you generate another sentence of less than 8 words describing a pathology image that shows basal cell carcinoma in a skin biopsy?"
    answers = ["Basal cell carcinoma is a type of skin cancer.",
               "Basal cell carcinoma is the diagnosis.",
               "Skin biopsy reveals basal cell carcinoma.",
               "The pathology tile shows basal cell carcinoma."]

    message_dict = append_question_and_answer(message_dict, 14, question, answers)

    # naevus
    message_dict[15] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 8 words describing a pathology image that shows naevus in a skin biopsy?"}]

    question = "Can you generate another sentence of less than 8 words describing a pathology image that shows naevus in a skin biopsy?"
    answers = ["H&E stained tile shows naevus in a skin biopsy.",
               "Naevus is a birthmark or mole in skin.",
               "Pathology tile shows naevus.",
               "Naevus is seen in the specimen from skin."]

    message_dict = append_question_and_answer(message_dict, 15, question, answers)
    return message_dict