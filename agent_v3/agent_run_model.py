from typing import List, Optional, Literal
from pydantic import BaseModel, ValidationError
from uuid import uuid4


class Question(BaseModel):
    id: int
    parent_id: int | None = None
    question: str
    answer: str | None = None
    documents: List | None = None
    status: Literal["current", "unanswered", "answered"] = "unanswered"


class AgentRunModel:
    _questions: List[Question]
    _answerpad: List[str]
    uuid: str
    status: Literal["init", "running", "finished"]
    goal_question_id = 0

    def __init__(self):
        self._questions = []
        self._answerpad = []
        self.uuid = str(uuid4())
        self.status = "init"

    def find_question(self, id: int) -> Question | None:
        qs = [q for q in self._questions if q.id == id]
        return None if len(qs) == 0 else qs[0]

    def set_goal(self, goal: str) -> Question:
        self.add_question({"id": self.goal_question_id, "question": goal})

    def goal(self) -> str:
        q = self.find_question(0).question
        return q if q else None

    def set_running(self):
        self.status = "running"

    def set_finished(self):
        self.status = "finished"

    def set_current_question(self, question_id: int):
        q = self.find_question(question_id)
        q.status = "current"
        return q

    def get_last_id(self) -> int:
        last_id = max([q.id for q in self._questions])
        return last_id

    def get_all_questions(self) -> List[Question]:
        return self._questions

    def get_answered_questions(self) -> List[Question]:
        qs = [q for q in self._questions if q.status == "answered"]
        return qs

    def get_unanswered_questions(self) -> List[Question]:
        qs = [q for q in self._questions if q.status == "unanswered"]
        return qs

    def get_current_question(self) -> Question:
        qs = [q for q in self._questions if q.status == "current"]
        return None if len(qs) == 0 else qs[0]

    def add_question(self, q_dict: dict):
        try:
            q = Question(**q_dict)
            self._questions.append(q)
        except ValidationError as e:
            print(e.errors())

    def add_questions(self, q_list: list):
        for q in q_list:
            self.add_question(q)

    def add_answer_to_question(self, question_id: int, answer: str, documents=None):
        q = self.find_question(question_id)
        if not q:
            return False
        q.answer, q.documents = answer, documents
        q.status = "answered"
        return True

    def add_answer_to_answerpad(self, answer: str):
        self._answerpad.append(answer)

    def get_answerpad(self) -> List[str]:
        return self._answerpad

    ## These functions should not be here.
    # def get_question_string(self, id: int):
    #     q = self.find_question(id)
    #     return None if q is None else q.question

    # def get_questions_string_list(self):
    #     q_list = [f"'{q.question}'" for q in self._questions]
    #     q_string_list = "[\n" + ",\n".join(q_list) + "\n]"
    #     return q_string_list
