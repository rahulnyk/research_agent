## Define Agent
##
from helpers.retriever import Retriever
from agent_run_model import AgentRunModel, Question

## Actions
from actions import select_next_question
from actions import ask_new_questions
from actions import answer_current_question
from actions import refine_goal_answer
from actions import create_initial_hypothesis

## Utils
from langchain_core.documents import Document
from typing import List


class Agent:
    def __init__(self, goal: str, retriever: Retriever, agent_settings: dict):
        self.agent_settings = agent_settings
        self.retriever = retriever
        self.run_model = AgentRunModel()
        self.model = agent_settings.get("model", "mistral-openorca:latest")
        self.max_iter = agent_settings.get("max_iter", 4)
        self.run_model.set_goal(goal)

    def get_docs(self, query: str) -> List[Document]:
        documents = self.retriever.get_docs(query)
        return documents

    def run(self):
        # Step 1: create a hypothesis and find initial Answer
        hyde_res = create_initial_hypothesis(self.run_model, self.agent_settings)
        hypothesis = f"{self.run_model.goal()}\n{hyde_res}"
        docs = self.get_docs(hypothesis)

        ## Step 2: Find Initial answer
        print("\n\nInitial Answer ▷▶\n")
        self.run_model.set_current_question(self.run_model.goal_question_id)
        answer = answer_current_question(self.run_model, self.agent_settings, docs)
        self.run_model.add_answer_to_answerpad(answer)
        parent_node_id = self.run_model.goal_question_id

        for current_iteration in range(1, self.max_iter + 1):
            print(f"\n\nIteration - {current_iteration}  ▷▶  \n")

            ## Step 3: Generate questions
            questions = ask_new_questions(
                self.run_model, self.agent_settings, parent_node_id
            )
            self.run_model.add_questions(questions)

            ## Step 4: Pick a question to answer next.
            next_quesition = select_next_question(self.run_model, self.agent_settings)
            self.run_model.set_current_question(next_quesition.id)
            parent_node_id = next_quesition.id

            ## Step 3: Answer the current Question.
            docs = self.get_docs(self.run_model.get_current_question().question)
            intermediate_q_answer = answer_current_question(
                self.run_model, self.agent_settings, docs
            )

            ## Step 5: Refine the answer
            refine_goal_answer(
                self.run_model, self.agent_settings, new_context=intermediate_q_answer
            )

        print("\n\nFinal Answer ▷▶\n", self.run_model.find_question(0).answer)
