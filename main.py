from schemas.llm_assistant import input, Response
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()


def prompt_builder(user_input: input) -> str:
    """Build a prompt from user input."""
    prompt = f"tell me about {user_input.input}"
    return prompt


def get_response(prompt: str) -> Response:

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        api_key=os.getenv("OPENAI_API_KEY"),
        temperature=0.7
    )
    
    prompt_template = ChatPromptTemplate.from_template(
        "You are a helpful assistant. {prompt}\n\n"
    )
    #guarantees the shape of the data, not how Python prints its
    #response is pydantic object not ai message
    chain = prompt_template | llm.with_structured_output(Response)
    #the process of making a request to an LLM service (typically via an API call) to generate a response, perform a task, or execute a function
    #chain.invoke() is a synchronous function call that sends an input to a "runnable" sequence (the chain) and waits for the complete final output. It is the standard way to run a task in a LangChain application built with the LangChain Expression Language (LCEL). 
    #validated_response is the final output of the chain
    validated_response = chain.invoke({"prompt": prompt})
    
    return validated_response
    # return Response(response=validated_response.response, confidence=validated_response.confidence, total_tokens=validated_response.total_tokens)

if __name__ == "__main__":
    user_input = input(input="how are you?")
    prompt = prompt_builder(user_input)
    response = get_response(prompt)
    print(response.model_dump_json())