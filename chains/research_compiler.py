from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

def research_compiler(llm, question: str, context: str, prev_answer: str, verbose: bool = True):
    prompt_template = (
    "Your task is to answer the users question"
    " Question: {question} \n"
    " You can use previously found incomplete answers (only if needed)"
    " Previous Answer: {prev_answer} \n"
    " Use the following context to create a complete and elaborate answer." 
    " Context: {context} \n"
    " The context includes answers to several similar questions"
    " Give an elaborate answer. don't try to make up an answer."
    " If you don't know the answer, just say that you don't know,"
    " Answer only based on the given information, and no other prior knowledge."
    " Answer :")

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question", "prev_answer"]
    )

    chain = LLMChain(
        llm=llm,
        prompt=PROMPT,
    )

    result = chain({"question": question, "context": context, "prev_answer": prev_answer})
    return result