import sys

sys.path.append("..")
import ollama.client as client


def retrievalQA(
    question: str,
    documents: str,
    model="mistral-openorca:latest",
):
    SYS_PROMPT = (
        "You will be provided with a 'question' and a list of 'excerpts' from a long document (delimited by ```)."
        " Your task is to answer the question based on the given documents excerpts."
        " Answer in a crisp, objective and business casual tone."
    )

    prompt = (
        f"Question:\n ``` {question} ```\n"
        f"Excerpts:\n ``` {documents} ```\n"
        "Your response:"
    )
    # print("\n---\n", SYS_PROMPT, prompt, "\n---\n")
    response, _ = client.generate(model_name=model, system=SYS_PROMPT, prompt=prompt)

    return response
