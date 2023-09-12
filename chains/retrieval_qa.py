from langchain.llms import BaseLLM
from langchain.base_language import BaseLanguageModel
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.vectorstores import PGVector
from langchain.chains import RetrievalQA

def retrieval_qa(llm, store: PGVector, question: str, verbose: bool = True):
    """
    This chain is used to answer the intermediate questions.
    """
    prompt_template = (
    "Use the following pieces of context" 
    " Context:"
    " {context}"
    " Your objective is to answer the following question"
    " Question:"
    " {question}"
    " Answer based only on the context and no other previous knowledge"
    " don't try to make up an answer."
    " If you don't know the answer, just say that you don't know,"
    " Answer in less than 200 words."
    " Answer :")

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm, 
        chain_type="stuff", 
        retriever=store.as_retriever(),
        return_source_documents=True,
        chain_type_kwargs={"prompt": PROMPT},
        verbose = verbose,
    )

    result = qa_chain({"query": question})
    return result['result'], result['source_documents']