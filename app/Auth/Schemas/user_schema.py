from typing import Optional
from pydantic import BaseModel, Field

from app.Auth.Enum.user_role import UserRoleEnum

class UserSchema(BaseModel):
     name: str
     lastname: str
     email: str
     institution_name: str
     profile_picture: str | None
     role: UserRoleEnum | None

class UpdateUserSchema(BaseModel):
    name: Optional[str]
    lastname: Optional[str]
    profile_picture: Optional[str]