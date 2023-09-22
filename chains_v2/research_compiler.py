from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

def research_compiler(llm, question: str, notes: str, verbose: bool = True):
    prompt_template = (
    "Your task is to write a clear, crisp and detailed answer for the following question\n"
    " Question: '{question}' \n"
    " You are provided with the following notes (delimited between '___'):\n" 
    " ___\n{notes}\n ___\n"
    " The notes include answers to several questions relevant to the original question."
    " Use the information from the notes that is most relevant to the original question"
    " Write the answer solely based on the give notes and no other provious knowledge."
    " Write an elaborate answer in less than 1200 words."
    " Answer :")

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["notes", "question"]
    )

    chain = LLMChain(
        llm=llm,
        prompt=PROMPT,
        verbose=verbose,
    )

    result = chain({"question": question, "notes": notes})
    return result