from typing import List  # Agregar esta importación
from fastapi import HTTPException
from pydantic import BaseModel, model_validator

from app.Auth.Enum.user_role import UserRoleEnum
from app.Campus.Schemas.campus_schema import CampusDetailResponse
from app.University.Validator.university_validator import UniversityValidator

class UniversityRequest(BaseModel):
    name: str 
    location: str
    contact: str 

    @model_validator(mode='before')
    def validate_university(cls, values):
   
        values['name'] = UniversityValidator.validate_name(values.get('name'))
        values['location'] = UniversityValidator.validate_location(values.get('location'))
        values['contact'] = UniversityValidator.validate_contact(values.get('contact'))
        return values
     
class UniversityResponse(BaseModel):
    id: int
    name: str
    location: str
    contact: str

class UniversityDetailResponse(BaseModel):
    id: int
    name: str
    location: str
    contact: str
    campuses: List[CampusDetailResponse]
    
    class Config:
        orm_mode = True

