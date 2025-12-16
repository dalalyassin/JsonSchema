from schemas.llm_assistant import input, Response
from openai import Client
import os
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
load_dotenv()
 
 
def prompt_builder(input: input) -> str:
    prompt = f"tell me about {input.input}"
    return prompt
 
 
def get_response(prompt: str) -> Response:
    pydantic_output_parser = PydanticOutputParser(pydantic_object=Response)
    format_instructions = pydantic_output_parser.get_format_instructions()
    client = Client(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt + format_instructions}]
    )
    return pydantic_output_parser.parse(response.choices[0].message.content)
   
 
prompt = prompt_builder(input(input="how are you?"))
print(get_response(prompt))
 