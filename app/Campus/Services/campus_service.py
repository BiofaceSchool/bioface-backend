
from sqlalchemy.orm import Session

from app.Campus.Models.campus_model import Campus
from app.Campus.Repository.campus_repository import CampusRepository
from app.Campus.Schemas.campus_schema import CampusRequest
from app.Faculties.Schemas.faculty_schema import FacultyResponse
from app.University.Models.university_model import University
from app.University.Repository.university_repository import UniversityRepository
from app.shared.Validator.error_factory import ValidationError

class CampusService: 
    def __init__(self, db: Session):
        self.university_repo = UniversityRepository(db)
        self.campus_repo = CampusRepository(db)

    
    def get_campus_by_id(self, id: int):
        campus = self.campus_repo.get_by_id(id)
        return campus
    
    def get_all_campuses(self):
        campuses = self.campus_repo.get_all()
        return campuses

    def add_campus(self, new_campus: CampusRequest, university_id: int):
        university : University = self.university_repo.get_by_id(university_id)

        for campus in university.campuses:
            if campus.name == new_campus.name:
                raise ValidationError("Campus with this name already exists")
            
        campus = Campus(**new_campus.dict(), university_id=university_id)    
        self.campus_repo.add(campus)

        return f"Campus {new_campus.name} successfully"

    def update_campus(self, campus: CampusRequest, id: int):
        campus = self.campus_repo.update(campus, id)
        return f"Campus {campus.name} updated successfully"
    
    def delete_campus(self, id: int):
        campus = self.campus_repo.delete(id)
        return campus
    
    def get_faculties_by_campus(self, campus_id: int):
        campus: Campus = self.campus_repo.get_by_id(campus_id)
        
        faculties: list[FacultyResponse] = campus.faculties

        return faculties