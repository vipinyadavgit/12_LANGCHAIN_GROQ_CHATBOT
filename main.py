import importlib
import sys
from pathlib import Path


src_dir = Path(__file__).parent / "src"
sys.path.insert(0, str(src_dir))

get_chain = importlib.import_module(
    "12_langchain_chatbot.chains"
).get_chain

def run_chat():
    chain = get_chain()

    ## Display instructions for the user
    print(
        "Groq langchain chatbot "
        "Type 'exit' to quit \n"
    )

    ## Continuously accept user input
    while True:
        user_input = input(
            "Pass medical queries: "
        )

        ## Exit condition
        if user_input.lower() == 'exit':
            break

        ## Invoke langchain pipeline
        try:
            response = chain.invoke({"input": user_input})
        except Exception as error:
            print(f"Request failed: {error}")
            print("Please check your GROQ_API_KEY and try again.\n")
            continue

        ## Display the final result
        print("Bot: ", response)

if __name__ == "__main__":
    run_chat()

