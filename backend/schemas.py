from typing import Optional

from pydantic import BaseModel


class UserSchema(BaseModel):
    id: Optional[int] = None
    login: str
    password: str
    first_name: str
    last_name: str
    email: str
    company_id: Optional[int] = None
