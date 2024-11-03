from datetime import datetime
from pydantic import BaseModel

from app.Auth.Enum.user_role import UserRoleEnum


class LoginResponse(BaseModel):
    id: str
    email: str
    role : str



class LoginRequest(BaseModel):
    email: str
    password: str

class TokenInfo(BaseModel):
    email: str
    id: str
    role : str
    exp : datetime