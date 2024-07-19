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

@router.post('/seed/', status_code=201)
def seed(db: Session= Depends(get_db)):
    cards = [
        Card(
        greek= 'Δικαιόπολις',
        english= 'Dicaiopolis',
        genitive_ending= 'ους',
        gender='Masculine',
        prepositional_case= None,
        example='Δικαιόπολις Ἀθηναῖός ἐστιν.',
        word_type='Proper noun',
        chapter='Iα'
        ),
        Card(
    greek= 'Ἀθηναῖoς',
    english= 'Athenian',
    genitive_ending= 'ου',
    gender= None,
    prepositional_case= None,
    example= 'Δικαιόπολις Ἀθηναῖός ἐστιν.',
    word_type= 'Adjective',
    chapter= 'Iα'),
        Card(
    id= 'o',
    greek= 'οἰκω',
    english= 'to live',
    genitive_ending= None,
    gender= None,
    prepositional_case= None,
    example= 'ὀ Δικαιόπολις οἰκεῖ οῦκ ἐν ταῖς Ἀθήναις.',
    word_type= 'Verb',
    chapter= 'Iα',
  ),
  Card(
    id= 'o',
    greek= 'ἐν',
    genitive_ending= None,
    gender= None,
    prepositional_case= 'Dative',
    example= 'οῦκ ἐν ταῖς Ἀθήναις.',
    english= 'in, at',
    word_type= 'Prespositional phrase',
    chapter= 'Iβ',
  ),
  Card(
    id= 'o',
    greek= 'εἰμι',
    genitive_ending= None,
    gender= None,
    prepositional_case= None,
    example= 'ἀνθπωπὸς κακὸς εἰμι.',
    english= 'to exist, be',
    word_type= 'Verb',
    chapter= 'Iβ',
  ),
  Card(
    id= 'o',
    greek= 'ἀγρός',
    genitive_ending= 'οῖς',
    gender= 'Masculine',
    prepositional_case= None,
    example= 'ὀ Δικαιόπολις οἰκεῖ ἐν τοῖς ἀγροῖς.',
    english= 'farm',
    word_type= 'Noun',
    chapter= 'Iβ',
  ),
  Card(
    id= 'o',
    greek= 'αὐτουργός',
    genitive_ending= 'οῦς',
    gender= 'Masculine',
    prepositional_case= None,
    example= 'αὐτουργὸς γάρ ἐστιν',
    english= 'landed farmer',
    word_type= 'Noun',
    chapter= '2α',
  ),
  Card(
    id= 'o',
    greek= 'γεωργῶ',
    genitive_ending= None,
    gender= 'Masculine',
    prepositional_case= None,
    example= 'Γεωργεῖ οὖν τὸν κλῆρον.',
    english= 'to cultivate, till',
    word_type= 'Noun',
    chapter= '2α',
  ) ]
    
    for card in cards:
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