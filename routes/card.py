from typing import List
import uuid
from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from models.card import Card
from pydantic_schemas.card_create import CardCreate
from pydantic_schemas.card_response import CardResponse
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/create", status_code=201)
def create(card: CardCreate, db: Session = Depends(get_db)):

    card_db = Card(
        id=str(uuid.uuid4()),
        greek=card.greek,
        english=card.english,
        example=card.example,
        gender=card.gender,
        word_type=card.word_type,
        genitive_ending=card.genitive_ending,
        prepositional_case=card.prepositional_case,
        chapter=card.chapter,
    )
    db.add(card_db)
    db.commit()
    db.refresh(card_db)

    return card_db

@router.get('/', status_code = 201, response_model=List[CardResponse])
def browse(db: Session=Depends(get_db)):
    cards = db.query(Card).all()
    
    return cards