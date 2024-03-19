from typing import Optional

from pydantic import BaseModel, model_validator, Json
from urllib.parse import parse_qs


class UserLoginSchema(BaseModel):
    email: str
    username: str
    password: str


class UserCreateSchema(BaseModel):
    email: str
    username: str
    password: str
    # TODO: remove magic number
    role_id: int = 2
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
