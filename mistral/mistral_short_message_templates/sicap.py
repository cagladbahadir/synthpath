# "sicap": ["benign glands",
#           "atrophic dense glands",
#           "cribriform ill-formed fused papillary patterns",
#           "isolated nest cells without lumen roseting patterns"
#           ],
# prostate


def append_question_and_answer(message_dict, key, question, answers):
    for i in range(len(answers)):
        message_dict[key].append({"role": "assistant", "content": answers[i]})
        message_dict[key].append({"role": "user", "content": question})
    return message_dict
def message_sicap():
    message_dict = {}

    # benign glands
    message_dict[0] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 8 words describing a pathology image that shows benign glands in prostate biopsy?"}]

    question = "Can you generate another sentence of less than 8 words describing a pathology image that shows benign glands in prostate biopsy?"

    answers = ["This image shows benign glands in the prostate.",
               "Biopsy from prostate reveals benign glands.",
               "Benign glands in the H&E stained sample from prostate.",
               "Pathology specimen shows benign glands in prostate."]

    message_dict = append_question_and_answer(message_dict, 0, question, answers)

    # atrophic dense glands
    message_dict[1] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 8 words describing a pathology image that shows atrophic glands in prostate biopsy?"}]

    question = "Can you generate another sentence of less than 8 words describing a pathology image that shows atrophic glands in prostate biopsy?"

    answers = ["Image shows atrophic dense glands in the prostate.",
               "Biopsy from the prostate reveals atrophic dense glands.",
               "Atrophic dense glands are visible in prostate H&E tile.",
               "Specimen shows atrophic dense glands in the prostate."]

    message_dict = append_question_and_answer(message_dict, 1, question, answers)

    # cribriform ill-formed fused papillary patterns
    message_dict[2] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 10 words describing a pathology image that shows cribriform ill-formed fused papillary patterns in prostate biopsy?"}]

    question = "Can you generate another sentence of less than 10 words describing a pathology image that shows cribriform ill-formed fused papillary patterns in prostate biopsy?"

    answers = ["Image of cribriform ill-formed fused papillary patterns in prostate.",
               "Prostate biopsy with cribriform ill-formed fused papillary patterns.",
               "H&E from prostate shows cribriform ill-formed fused papillary patterns.",
               "Cribriform ill-formed fused papillary patterns in the prostate."]

    message_dict = append_question_and_answer(message_dict, 2, question, answers)

    # isolated nest cells without lumen roseting patterns
    message_dict[3] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 10 words describing a pathology image that shows isolated nest cells without lumen roseting patterns in prostate biopsy?"}]

    question = "Can you generate another sentence of less than 10 words describing a pathology image that shows isolated nest cells without lumen roseting patterns in prostate biopsy?"

    answers = ["Isolated nest cells without lumen roseting patterns in the prostate.",
               "Prostate biopsy showing isolated nest cells without lumen roseting patterns.",
               "Isolated nest cells without lumen roseting patterns in H&E stained prostate.",
               "Specimen shows isolated nest cells without lumen roseting patterns in prostate."]

    message_dict = append_question_and_answer(message_dict, 3, question, answers)


    return message_dict