from sqlalchemy.orm import Session
from . import models, schemas


def get_users(db: Session):
    return db.query(models.User).all()


def get_user(user_id: int,
             db: Session):
    return db.query(models.User).filter_by(id=user_id).one()
