# 12_LANGCHAIN_CHATBOT

run command 
cd "D:\Projects\GenAI projects\12_LANGCHAIN_CHATBOT"
uv run python main.py

    USER
     |
main.py
     |
prompt template (prompts.py)
     |
ChatGroq (llm.py)
     |
StrOutputParser  (chains.py)
     |
    User  

1. config.py   (load env and keys)
2. llm.py      (created llm object and calls keys and model)
3. prompts.py  (defined prompts(system & user))
4. chains.py    (call everything here to create pipeline)