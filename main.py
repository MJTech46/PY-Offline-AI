from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import GPT4All
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

#orginal
#template = """Please act as a geographer. Please provide the answer in a short way. Question: {question}"""

#(recommended)
template = "Please act as an assistant. Please provide the answer in a short way. Question: {question}"

#(not recommended)
#template = "Please act as an assistant. Please provide the answer in a detailed way. Question: {question}"

prompt = PromptTemplate(template=template, input_variables=["question"])

local_path = ("./mistral-7b-instruct-v0.1.Q3_K_M.gguf")

callbacks = [StreamingStdOutCallbackHandler()]

llm = GPT4All(model=local_path, callbacks=callbacks, verbose=True)
llm = GPT4All(model=local_path, backend="gptj", callbacks=callbacks, verbose=True)
llm_chain = LLMChain(prompt=prompt, llm=llm)

print("Model loaded :)")

#question = "What is the capital of France?" #orginal question

while True:  # Infinite loop
    question = input("\nEnter your question: ")
    # Important string additions for correct processing by Mistral Instruct
    str1 = "###Human:\\n"
    str2 = "\\n###Assistant:"
    llm_chain.run(str1 + question + str2)