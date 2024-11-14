
from pydantic import BaseModel, model_validator

from app.Faculties.Validator.faculty_validator import FacultyValidator

class FacultyRequest(BaseModel):
    name: str

    class Config:
        orm_mode = True  

    @model_validator(mode='before')
    def validate_university(cls, values):
        values['name'] = FacultyValidator.validate_name(values.get('name'))
        return values

class FacultyResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True  