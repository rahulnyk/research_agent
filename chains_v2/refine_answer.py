from langchain.llms import BaseLLM
from langchain.base_language import BaseLanguageModel
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate


class RefineAnswer(LLMChain):
    """
    This chain splits the original question into a set of atomistic questions.
    """

    @classmethod
    def from_llm(cls, llm: BaseLanguageModel, verbose: bool = True) -> LLMChain:
        """Get the response parser."""
        prompt_template = (
            "Your are provided with a question and an exsiting answer.\n"
            " Question: '{question}'\nExisting Answer: \n----\n{answer}\n----\n"
            " Your team has provided you with some additional context that may be relevant to the question."
            " New Context: \n----\n{context}\n----\n"
            " You have the opportunity to rewrite and improve upon the existing answer."
            " Use only the information from the existing answer and the context to write better answer."
            " If the context isn't useful, return the existing answer."
        )
        prompt = PromptTemplate(
            template=prompt_template,
            input_variables=["question", "answer", "context"],
        )
        return cls(prompt=prompt, llm=llm, verbose=verbose)
