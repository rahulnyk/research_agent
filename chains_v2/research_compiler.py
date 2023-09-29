from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

def research_compiler(llm, question: str, notes: str, answer_length: int, verbose: bool = True):
    # prompt_template = (
    # "You are a researcher. Your task is to answer the following question\n"
    # " Question: '{question}' \n"
    # " You are provided with some notes (delimited between '___')"
    # " ___\n{notes}\n ___\n"
    # " The notes include answers to several questions that may be relevant to the original question."
    # " Use only the information from the notes that is most pertinent to the question."
    # " Write the answer solely based on the give notes and no other provious knowledge."
    # " Answer should be clear, crisp and detailed."
    # " Write your answer in less than {answer_length} words."
    # " Answer :")
    prompt_template = (
        "You are a research agent who answers complex questions with clear, crisp and detailed answers."
        " You are provided with a question and some research notes prepared by your team."
        " Question: {question} \n"
        " Notes: {notes} \n"
        " Your task is to answer the question entirely based on the given notes."
        " The notes contain a list of intermediate-questions and answers that may be helpful to you in writing an answer."
        " Use only the most relevant information from the notes while writing your answer."
        " Do not use any prior knowledge while writing your answer, Do not make up the answer."
        " If the notes are not relevant to the question, just return 'Context is insufficient to answer the question'."
        " Remember your goal is to answer the question as objectively as possible."
        " Write your answer succinctly in less than {answer_length} words."
    )

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["notes", "question", "answer_length"]
    )

    chain = LLMChain(
        llm=llm,
        prompt=PROMPT,
        verbose=verbose,
    )

    result = chain({"question": question, "notes": notes, "answer_length": answer_length})
    return result