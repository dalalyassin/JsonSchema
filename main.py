from pydantic.type_adapter import P
from schemas.llm_assistant import input, Response
from openai import Client
import os
from dotenv import load_dotenv

load_dotenv()


def prompt_builder(input: input) -> str:
    prompt = f"tell me about {input.input}"
    return prompt


def get_response(prompt: str) -> Response:
    client = Client(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return Response(response=response.choices[0].message.content).model_dump_json()
    

prompt = prompt_builder(input(input="how are you?"))
print(get_response(prompt))