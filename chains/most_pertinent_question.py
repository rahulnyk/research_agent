
from langchain.llms import BaseLLM
from langchain.base_language import BaseLanguageModel
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

class MostPertinentQuestion(LLMChain):
    """
    This chain picks one question out of a list of questions
    most pertinent to the original question. 
    """

    @classmethod
    def from_llm(cls, llm: BaseLanguageModel, verbose: bool = True) -> LLMChain:
        """Get the response parser."""
        task_prioritization_template = (
            "You are provided with the following list of questions:"
            " {unanswered_questions} \n"
            " Your task is to find one question from the given list" 
            " that is the most pertinent to the following query" 
            " {original_question} \n"
            " Respond with one question out of the provided list of questions"
            " Return the questions as it is without any edits"
            " Format your response like:"
            " #. question"
        )
        prompt = PromptTemplate(
            template=task_prioritization_template,
            input_variables=["unanswered_questions", "original_question"],
        )
        return cls(prompt=prompt, llm=llm, verbose=verbose)