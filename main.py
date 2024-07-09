from fastapi import FastAPI
from models.base import Base
from routes import card
from models.base import Base
from database import engine

app = FastAPI()

app.include_router(router=card.router, prefix='/card')

Base.metadata.create_all(engine)
