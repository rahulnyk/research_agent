def qStr2Dict(question: str) -> dict:
    # print('qStr2Dict :', question)
    split = question.strip(" '\"").split(".", 1)
    question_dict = {'id': int(split[0]), 'question': split[-1].strip()}
    return question_dict


def result2QuestionsList(question_response: str, type: str, status: str) -> list:
    response_splits = question_response.split("\n")
    qlist = []
    for q in response_splits:
        question = {**qStr2Dict(q), 'type': type, 'status': status, 'answer': None}
        qlist = qlist + [question]
    return qlist