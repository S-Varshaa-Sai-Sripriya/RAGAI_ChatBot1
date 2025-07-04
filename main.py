from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3.2")

template = """

You are an expert in answering questions about this restaurant's menu especially pizzas!.

Here are some relavant reviews: {reviews}

Here is the question to answer: {question}

""" 

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

while True:
    print("\n\n------------------------------------------------")
    user_input = input("Ask your question or type 'q' to quit: ")
    print("\n\n------------------------------------------------")
    if user_input.lower() == 'q':
        break
    else:
        reviews = retriever.invoke(user_input)
        results = chain.invoke({"reviews":[],
                        "question":user_input})
        print(results)