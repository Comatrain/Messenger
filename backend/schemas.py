from typing import Optional

from pydantic import BaseModel


class UserSchema(BaseModel):
    id: Optional[int] = None
    email: str
    username: str
    password: str
    role_id: int = 1
