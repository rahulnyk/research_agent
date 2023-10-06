# from langchain.llms import BaseLLM
# from langchain.base_language import BaseLanguageModel
# from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.vectorstores import PGVector
from langchain.chains import RetrievalQA

def retrieval_qa(llm, retriever: PGVector, question: str, answer_length: 250, verbose: bool = True):
    """
    This chain is used to answer the intermediate questions.
    """
    prompt_answer_length = f" Answer as succinctly as possible in less than {answer_length} words.\n"

    prompt_template = \
        "You are provided with a question and some helpful context to answer the question \n" \
        " Question: {question}\n" \
        " Context: {context}\n" \
        "Your task is to answer the question based in the information given in the context" \
        " Answer the question entirely based on the context and no other previous knowledge." \
        " If the context provided is empty or irrelevant, just return 'Context not sufficient'"\
        + prompt_answer_length

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm, 
        chain_type="stuff", 
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": PROMPT},
        verbose = verbose,
    )

    result = qa_chain({"query": question})
    return result['result'], result['source_documents']