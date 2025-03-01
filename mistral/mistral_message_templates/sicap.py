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
         "content": "Can you generate a single sentence of less than 15 words describing a pathology image that shows benign glands in prostate biopsy?"}]

    question = "Can you generate another sentence of less than 15 words describing a pathology image that shows benign glands in prostate biopsy?"

    answers = ["This image shows benign glands in the prostate.",
               "The biopsy from the prostate reveals benign glands.",
               "The benign glands are visible in the H&E stained sample from the prostate.",
               "The pathology specimen shows benign glands in the prostate."]

    message_dict = append_question_and_answer(message_dict, 0, question, answers)

    # atrophic dense glands
    message_dict[1] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 15 words describing a pathology image that shows atrophic glands in prostate biopsy?"}]

    question = "Can you generate another sentence of less than 15 words describing a pathology image that shows atrophic glands in prostate biopsy?"

    answers = ["This image shows atrophic dense glands in the prostate.",
               "The biopsy from the prostate reveals atrophic dense glands.",
               "The atrophic dense glands are visible in the H&E stained sample from the prostate.",
               "The pathology specimen shows atrophic dense glands in the prostate."]

    message_dict = append_question_and_answer(message_dict, 1, question, answers)

    # cribriform ill-formed fused papillary patterns
    message_dict[2] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 15 words describing a pathology image that shows cribriform ill-formed fused papillary patterns in prostate biopsy?"}]

    question = "Can you generate another sentence of less than 15 words describing a pathology image that shows cribriform ill-formed fused papillary patterns in prostate biopsy?"

    answers = ["This image shows cribriform ill-formed fused papillary patterns in the prostate.",
               "The biopsy from the prostate reveals cribriform ill-formed fused papillary patterns.",
               "The cribriform ill-formed fused papillary patterns are visible in the H&E stained sample from the prostate.",
               "The pathology specimen shows cribriform ill-formed fused papillary patterns in the prostate."]

    message_dict = append_question_and_answer(message_dict, 2, question, answers)

    # isolated nest cells without lumen roseting patterns
    message_dict[3] = [
        {"role": "user",
         "content": "Can you generate a single sentence of less than 15 words describing a pathology image that shows isolated nest cells without lumen roseting patterns in prostate biopsy?"}]

    question = "Can you generate another sentence of less than 15 words describing a pathology image that shows isolated nest cells without lumen roseting patterns in prostate biopsy?"

    answers = ["This image shows isolated nest cells without lumen roseting patterns in the prostate.",
               "The biopsy from the prostate reveals isolated nest cells without lumen roseting patterns.",
               "The cisolated nest cells without lumen roseting patterns are visible in the H&E stained sample from the prostate.",
               "The pathology specimen shows isolated nest cells without lumen roseting patterns in the prostate."]

    message_dict = append_question_and_answer(message_dict, 3, question, answers)


    return message_dict