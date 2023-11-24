from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import GPT4All
from langchain.chains.conversation.memory import ConversationSummaryMemory

template = "Please act as an assistant. Please provide the answer in a short way. Question: {question}"
prompt = PromptTemplate(template=template, input_variables=["question"])
local_path = "./mistral-7b-instruct-v0.1.Q3_K_M.gguf"

# Removed the StreamingStdOutCallbackHandler from callbacks
llm = GPT4All(model=local_path, verbose=True)

# Initialize the conversation chain with conversational memory
conversation = LLMChain(prompt=prompt, llm=llm, memory=ConversationSummaryMemory(llm=llm))

conversation_history = ""  # Initialize an empty conversation history

while True:  # Infinite loop
    question = input("You: ")
    str1 = "###Human:\\n"
    str2 = "\\n###Assistant:"
    conversation_history += str1 + question + str2  # Append the user's question to the conversation history
    response = conversation.run(conversation_history)  # Pass the conversation history to the model
    conversation_history += response  # Append the model's response to the conversation history
    print("Assistant: ", response.split(str2)[-1].split("\\n")[0])  # Print only the model's response

