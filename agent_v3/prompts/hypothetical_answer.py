import sys

sys.path.append("..")
import ollama.client as client


def hyDE(
    question: str,
    model="mistral-openorca:latest",
):
    SYS_PROMPT = (
        "You will be provided with a 'question'."
        " Your task is to create a hypothesis on what information is required to answer the 'question'."
        " The hypothesis will be used to search a large document for context relevant to the question."
        " You can use the following chain of thoughts:\n"
        " \tThought 1: Concepts. What are the entities like subject, predicate, etc. mentioned in the question?\n"
        " \tThought 2: Context. What additional context may help you know more about these entities to answer the question?\n"
        " Do not use any prior knowledge. If it is not possible to make a hypothesis, return the original question."
        " Format your answer as the following: \n"
        " Concepts: \n"
        " Context: \n"
        # " {\"Concepts\": \"a list of concepts\", \"Context\": \" \"}"
    )

    prompt = f"Question: ``` {question} ```\n Your response:"

    response, _ = client.generate(model_name=model, system=SYS_PROMPT, prompt=prompt)

    return response
