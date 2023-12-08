import sys

sys.path.append("..")
import ollama.client as client


def refineAnswer(
    question: str,
    answer: str,
    context: str,
    model="mistral-openorca:latest",
):
    SYS_PROMPT = (
        "You will be provided with a 'question', an 'existing answer', and some 'new context'"
        " You have the opportunity to improve upon the 'existing answer'"
        " Using the following chain of thought:\n"
        "\t - Is the 'new context' relevant to the 'question'?.\n"
        "\t - Is there any new information in the 'new context' that can be added to the 'existing answer'?\n"
        "\t - Are there any corrections needed to the 'existing answer' based on 'new context'\n"
        "\t - Can you augment or correct the 'existing answer' using the 'new context'?\n"
        " Refine the 'existing answer' only if needed. Use only the given context. Do not use any pre-existing knowledge.\n"
        " Respond with a new answer"
        " Use a descriptive style and a business casual language."
    )

    prompt = (
        f"Question: ``` {question} ```\n"
        f"Existing Answer: ``` {answer} ```\n"
        f"New Context: ``` {context} ```\n"
        "New Answer:"
    )

    response, _ = client.generate(model_name=model, system=SYS_PROMPT, prompt=prompt)

    return response
