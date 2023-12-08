import json


def question_str_to_dict(question: str) -> dict:
    split = question.strip(" '\"").split(".", 1)
    question_dict = {"id": int(split[0]), "question": split[-1].strip()}
    return question_dict


def result_to_questions_list(
    question_response: str, start_id: int, parent_id: int
) -> list:
    qlist = eval(question_response)
    questions = []
    question_id = start_id
    for q in qlist:
        questions += [
            {
                "id": question_id,
                "parent_id": parent_id,
                "question": q,
                "status": "unanswered",
            }
        ]
        question_id += 1

    return questions


def parse_json(response: str) -> dict:
    try:
        output_dict = json.loads(response)
        return output_dict
    except:
        print("Could not parse into json :", response)

