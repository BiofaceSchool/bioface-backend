from pydantic import BaseModel, Field

class RegisterRequest(BaseModel):
    name: str
    lastname: str
    email: str
    password: str
    institution_name: str