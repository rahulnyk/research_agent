from langchain.llms import BaseLLM
from langchain.base_language import BaseLanguageModel
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate


class QuestionCreationChain(LLMChain):
    """Chain to generates subsequent questions."""

    @classmethod
    def from_llm(cls, llm: BaseLLM, verbose: bool = True) -> LLMChain:
        task_creation_template = (
            "You are a part of a team. The ultimate goal of your team is to "
            "answer the following query - '{question}'.\n"
            "Your team has discovered some new text that may be relevant to your ultimate goal.\n"
            "text: ### {context} ### \n\n"
            "Your task is to ask new questions that may help your team achieve the ultimate goal. "
            "If you think that the text is relevant to your ultimate goal, then "
            "ask new questions solely based on the text and no other privious knowledge. "
            "If not, then return 'Not Relevant'. "
            "The new questions should have no overlap with these questions:\n"
            "{previous_questions}\n"
            "You can ask up to {num_questions} new questions. "
            "Return the questions as a comma separated list. "
            "Format your response as a numbered list of questions, like:\n"
            "n. First question\n"
            "n. Second question\n"
            "Start the list with number {start_id}"
        )

        prompt = PromptTemplate(
            template=task_creation_template,
            input_variables=[
                "question",
                "context",
                "previous_questions",
                "num_questions",
                "start_id",
            ],
        )
        return cls(prompt=prompt, llm=llm, verbose=verbose)
