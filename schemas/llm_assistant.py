from typing import Optional
from pydantic import BaseModel

class input(BaseModel):
    input: str

class Response(BaseModel):
    response: str
    confidence:  float
    total_tokens: int
    

  