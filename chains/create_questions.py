
from langchain.llms import BaseLLM
from langchain.base_language import BaseLanguageModel
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

class QuestionCreationChain(LLMChain):
    """Chain to generates subsequent questions."""

    @classmethod
    def from_llm(cls, llm: BaseLLM, verbose: bool = True) -> LLMChain:
        """Get the response parser."""
        task_creation_template = (
            "You are a research agent who is provided with a user query and some context"
            " User query: {question}"
            " Context: {context}"
            " Your task is to ask questions which can help your team research on the users query"
            " These are previously asked unanswered questions: {unanswered_questions}."
            " You can ask only upto {num_questions} new questions"
            " The new questions should have no overlap with the previously unanswered questions."
            " Return the questions as a comma separated list."
            " Format your response as a numbered list of questions, like:"
            " #. First question"
            " #. Second question"
            " Start the list with number {start_id}"
        )
        prompt = PromptTemplate(
            template=task_creation_template,
            input_variables=[
                "question",
                "context",
                "unanswered_questions",
                "num_questions",
                "start_id",
            ],
        )
        return cls(prompt=prompt, llm=llm, verbose=verbose)