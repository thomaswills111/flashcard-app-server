from sqlalchemy import TEXT, VARCHAR, Column
from models.base import Base

class Card(Base):
    __tablename__ = 'cards'
    id = Column(TEXT, primary_key = True)
    greek = Column(TEXT)
    example = Column(TEXT)
    english = Column(TEXT)
    gender = Column(TEXT)
    chapter = Column(TEXT)
    word_type =  Column(TEXT)
    genitive_ending =  Column(TEXT)
    prepositional_case =  Column(TEXT)