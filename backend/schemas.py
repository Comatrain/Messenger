from typing import Optional

from pydantic import BaseModel, ConfigDict


class UserSchema(BaseModel):
    id: Optional[int] = None
    name: str
    password: str
    first_name: str
    last_name: str
    email: str
    company_id: int | None = None

    model_config = ConfigDict(from_attributes=True)
