import sys

sys.path.append("..")
import ollama.client as client


def mostPertinentQuestion(
    question: str,
    unanswered_questions: str,
    model="mistral-openorca:latest",
):
    SYS_PROMPT = (
        "You are a curious researcher. Your task is to choose one question "
        "from a given list of 'unanswered questions' (delimited by ```). "
        "You are provided with a 'goal question' and a numbered list of 'unanswered questions' as inputs. "
        "Think about which question out of the given list of questions can help you answer the 'goal question'. "
        "Choose one and only one question from the list of 'unanswered questions'.\n"
        "Respond with the choosen question as it is, ditto without any edits."
        " Remember the format of the output should look like:\n"
        " question_id. question"
    )

    prompt = (
        f"Goal Question: ``` {question} ```.\n\n"
        f"Unanswered Questions:  ``` {unanswered_questions} ```\n\n"
        "Your response:"
    )

    response, _ = client.generate(model_name=model, system=SYS_PROMPT, prompt=prompt)

    return response
