
getAnsweredQuestions = lambda questions: [
    q for q in questions if q["status"] == "answered"
]
getUnansweredQuestions = lambda questions: [
    q for q in questions if q["status"] == "unanswered"
]
getSubQuestions = lambda questions: [q for q in questions if q["type"] == "subquestion"]
getHopQuestions = lambda questions: [q for q in questions if q["type"] == "hop"]
getLastQuestionId = lambda questions: max([q["id"] for q in questions])


def markAnswered(questions, id: int):
    for q in questions:
        if q["id"] == id:
            q["status"] = "answered"


def getQuestionById(questions, id: int):
    q = [q for q in questions if q["id"] == id]
    if len(q) == 0:
        return None
    return q[0]