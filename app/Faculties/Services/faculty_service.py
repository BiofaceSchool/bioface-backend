
from app.Campus.Models.campus_model import Campus
from app.Campus.Repository.campus_repository import CampusRepository
from app.Faculties.Models.faculty_model import Faculty
from app.Faculties.Repository.faculty_repository import FacultyRepository
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from app.Faculties.Schemas.faculty_schema import FacultyRequest
from app.shared.Validator.error_factory import ValidationError

class FacultyService: 
    def __init__(self, db: Session):
        self.faculty_repo = FacultyRepository(db)
        self.campus_repo = CampusRepository(db)

    
    def get_faculty_by_id(self, id: int):
        faculty = self.faculty_repo.get_by_id(id)
        return faculty
    
    def get_all_faculties(self):
        faculties = self.faculty_repo.get_all()
        return faculties


    def add_faculty(self, new_faculty: FacultyRequest, campus_id: int):
        campus : Campus = self.campus_repo.get_by_id(campus_id)

        for faculty in campus.faculties:
            if faculty.name == new_faculty.name:
                raise ValidationError("Faculty with this name already exists")
            
        faculty = Faculty(**new_faculty.dict(), campus_id=campus_id)    
        self.faculty_repo.add(faculty)

        return f"Faculty {new_faculty.name} successfully"

    def update_faculty(self, faculty: FacultyRequest, id: int):
        faculty = self.faculty_repo.update(faculty, id)
        return f"Faculty {faculty.name} updated successfully"
    
    def delete_faculty(self, id: int):
        faculty = self.faculty_repo.delete(id)
        return faculty