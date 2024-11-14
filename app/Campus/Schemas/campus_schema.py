
from pydantic import BaseModel, model_validator

from app.Faculties.Schemas.faculty_schema import FacultyResponse
from app.Faculties.Validator.faculty_validator import FacultyValidator

class CampusRequest(BaseModel):
    name: str

    class Config:
        orm_mode = True  

    @model_validator(mode='before')
    def validate_university(cls, values):
        values['name'] = FacultyValidator.validate_name(values.get('name'))
        return values

class CampusResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True  

class CampusDetailResponse(BaseModel):
    id: int
    name: str
    faculties: list[FacultyResponse]

    class Config:
        orm_mode = True

