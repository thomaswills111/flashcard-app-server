from pydantic import BaseModel
from typing import Optional

class CardCreate(BaseModel):
    greek: str
    english: str
    example: str
    gender: Optional[str]
    chapter: str
    word_type: Optional[str]
    genitive_ending: Optional[str]
    prepositional_case: Optional[str]
    