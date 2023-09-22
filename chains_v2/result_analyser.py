# def analyser(llm, original_question: str, answered_questions: str, unanswered_questions: str, verbose: bool = True):
#     prompt_template = (
#     "You are a research assistant provided with the users question," 
#     " previously answered questions, and some yet unanswered questions."
#     " users question:"
#     " {original_question} \n"
#     " answered questions:"
#     " {answered_questions} \n"
#     " unanswered questions:"
#     " {unanswered_questions} \n"
#     " Your task is to decide if the users question can be aptly "
#     " answered based on the answered to the previously answered questions."
#     " If you think the answers to the answered questions are enough to answer the users question," 
#     " and unanswered questions are not necessary, then answer with a 'Yes'. \n"
#     " Otherwise answer with a 'No'."
#     " Answer only in a 'Yes' or a 'No'."
#     )

#     PROMPT = PromptTemplate(
#         template=prompt_template, input_variables=["original_question", "answered_questions", "unanswered_questions"]
#     )

#     chain = LLMChain(
#         llm=llm,
#         prompt=PROMPT,
#     )

#     result = chain({
#         "original_question": original_question, 
#         "answered_questions": answered_questions, 
#         "unanswered_questions": unanswered_questions})
        
#     return result


# result = analyser(
#     llm = ChatOpenAI(model_name=gpt3t, temperature=0.1),
#     original_question = scratchpad['original_question'], 
#     answered_questions = scratchpad['answered_questions'], 
#     unanswered_questions = scratchpad['unanswered_questions'],
#     verbose = verbose)

# result