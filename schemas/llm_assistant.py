from typing import Optional
from pydantic import BaseModel

class input(BaseModel):
    input: str

class Response(BaseModel):
    response: str
    confidence: Optional[float] = None
    total_tokens: Optional[int] = None
    

  