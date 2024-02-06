from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .session import get_db
from . import crud

app = FastAPI()


@app.get("/users")
async def root(db: Session = Depends(get_db)):
    return crud.get_users(db=db)
