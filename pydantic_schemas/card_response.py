from pydantic import BaseModel
from typing import Optional

class CardResponse(BaseModel):
    id: str
    greek: str
    english: str
    example: str
    gender: Optional[str]
    chapter: str
    word_type: Optional[str]
    genitive_ending: Optional[str]
    prepositional_case: Optional[str]
    
    class Config:
        orm_mode = True