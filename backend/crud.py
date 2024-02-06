from sqlalchemy.orm import Session
from . import models, schemas


def get_users(db: Session):
    return db.query(models.User).all()
