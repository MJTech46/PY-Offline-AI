from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import GPT4All

##Template##
#template = "Please act as a geographer. Please provide the answer in a short way. Question: {question}" #orginal
template = "Please act as an assistant. Please provide the answer in a short way. Question: {question}" #(recommended)
#template = "Please act as an assistant. Please provide the answer in a detailed way. Question: {question}" #(not recommended)

prompt = PromptTemplate(template=template, input_variables=["question"])
local_path = ("./mistral-7b-instruct-v0.1.Q3_K_M.gguf")
llm = GPT4All(model=local_path, backend="gptj", verbose=True)
llm_chain = LLMChain(prompt=prompt, llm=llm)
print("Model loaded :)")

while True:  # Infinite loop
    question = input("\nYou: ")
    if question == 'exit':
        break
    # Important string additions for correct processing by Mistral Instruct
    str1 = "###Human:\\n"
    str2 = "\\n###Assistant:"
    response = llm_chain.run(str1 + question + str2)
    print("AI:",response)