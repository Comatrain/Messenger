from typing import Optional

from pydantic import BaseModel, model_validator, Json
from urllib.parse import parse_qs


class UserLoginSchema(BaseModel):
    username: str
    # TODO: add validate hash password (after convert to bytes)
    password: str


class UserRegisterSchema(UserLoginSchema):
    email: str


class UserCreateSchema(BaseModel):
    email: str
    username: str
    # TODO: add validate hash password (after convert to bytes)
    hashed_password: bytes
    salt: bytes
    # TODO: remove magic number
    role_id: int = 2
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False


# TODO: add validation for user.id
class CookieSessionCreateSchema(BaseModel):
    username_id: int
    cookie: str
