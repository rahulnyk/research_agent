from langchain.llms import BaseLLM
from langchain.base_language import BaseLanguageModel
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate


class RefineAnswer(LLMChain):
    """
    This refines the answer with every iteration.
    """

    @classmethod
    def from_llm(cls, llm: BaseLanguageModel, verbose: bool = True) -> LLMChain:
        """Get the response parser."""
        prompt_template = (
            "Your task is to answer the following question. and an exsiting answer.\n"
            " Question: '{question}'\n"
            " You are provided with an existing Answer: \n---\n{answer}\n---\n\n"
            " You are also provided with some additional context that may be relevant to the question.\n"
            " New Context: \n---\n{context}\n---\n\n"
            " You have the opportunity to rewrite and improve upon the existing answer."
            " Use only the information from the existing answer and the given context to write better answer."
            " Use a descriptive style and a business casual language."
            " If the context isn't useful, return the existing answer."
        )
        prompt = PromptTemplate(
            template=prompt_template,
            input_variables=["question", "answer", "context"],
        )
        return cls(prompt=prompt, llm=llm, verbose=verbose)
