from typing import Optional

from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    email: str
    username: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False


class UserCreateSchema(BaseModel):
    email: str
    username: str
    password: str
    # TODO: remove magic number
    role_id: int = 2
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
