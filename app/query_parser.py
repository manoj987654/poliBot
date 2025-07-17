
import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

def parse_query(user_input):
    openai_key = os.getenv("OPENAI_API_KEY")
    llm = ChatOpenAI(temperature=0, openai_api_key=openai_key, model_name="gpt-4")

    template = """
    Extract the following from the query:
    - age
    - gender
    - procedure
    - location
    - policy duration (months)

    Query: {query}

    Return in JSON format:
    {{
        "age": ...,
        "gender": "...",
        "procedure": "...",
        "location": "...",
        "policy_duration_months": ...
    }}
    """
    prompt = PromptTemplate(input_variables=["query"], template=template)
    response = llm.predict(prompt.format(query=user_input))
    return eval(response)
