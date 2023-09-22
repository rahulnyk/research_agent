
from langchain.llms import BaseLLM
from langchain.base_language import BaseLanguageModel
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate


class QuestionAtomizer(LLMChain):
    """
    This chain splits the original question into a set of atomistic questions. 
    """

    @classmethod
    def from_llm(cls, llm: BaseLanguageModel, verbose: bool = True) -> LLMChain:
        """Get the response parser."""
        task_prioritization_template = (
            " Your are provided with the following question:"
            " '{question}' \n"
            " Your task is to split the given question in at most {num_questions} very"
            " simple, basic and atomist sub-questions (only if needed) using only the"
            " information given in the question and no other prior knowledge."
            " The sub-questions should be directly related to the intent of the original question."
            " Consider the primary subject and the predicate of the question (if any) when creating sub questions.\n"
            " Consider also the Characters, Ideas, Concepts, Entities, Actions, Or Events mentioned"
            " in the question (if any) when creating the sub questions.\n"
            " The sub questions should have no semantic overlap with each other."
            " Format your response like: \n"
            " n. question"
        )
        prompt = PromptTemplate(
            template=task_prioritization_template,
            input_variables=["question", "num_questions"],
        )
        return cls(prompt=prompt, llm=llm, verbose=verbose)
