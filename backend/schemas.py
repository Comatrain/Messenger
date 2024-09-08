from typing import Optional

from pydantic import BaseModel


class AccountSchema(BaseModel):
    id: Optional[int] = None
    login: str
    password: str


class UserSchema(BaseModel):
    id: Optional[int] = None
    account_login: str
    first_name: str
    last_name: str
    email: str
    company_id: Optional[int] = None
