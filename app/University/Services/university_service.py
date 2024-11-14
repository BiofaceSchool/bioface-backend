from app.Campus.Repository.campus_repository import CampusRepository
from app.Campus.Schemas.campus_schema import CampusDetailResponse
from app.Faculties.Repository.faculty_repository import FacultyRepository
from app.Faculties.Schemas.faculty_schema import FacultyResponse
from app.University.Models.university_model import University
from app.University.Repository.university_repository import UniversityRepository
from sqlalchemy.orm import Session

from app.University.Schemas.university_schema import UniversityDetailResponse, UniversityRequest, UniversityResponse
from app.University.Validator.university_validator import UniversityValidator


class UniversityService:
    def __init__(self, db: Session):
        self.university_repo = UniversityRepository(db)
        self.campus_repo = CampusRepository(db)
        self.faculty_repo = FacultyRepository(db)

    def get_university_by_id(self, id: int):
        uni =  self.university_repo.get(id)
        uni = UniversityResponse(**uni.to_dict())
        return uni
    
    def add_university(self, university: UniversityRequest):
        try:

            new_university = University(**university.dict())
            self.university_repo.add(new_university)

            new_university = UniversityResponse(**new_university.to_dict()) 

            return new_university
        except Exception as e:
            return {"message": {"error": str(e)}}   
    
    def update_university(self, university: UniversityRequest, id: int, ):
        
        university = self.university_repo.update(university, id)
        university = UniversityResponse(**university.to_dict())
        return university
    
    def delete_university(self, id: int):
        university: UniversityResponse = self.university_repo.delete(id)
        return {"message": f"University {university.name} deleted successfully"}

    def get_by_name(self, name: str):
        university = self.university_repo.get_by_attribute("name", name)
        university = UniversityResponse(**university.to_dict())
        return university

    def get_all_universities(self):
        universities = self.university_repo.get_all()
        return universities
    
    def get_university_campuses(self, university_id: int):
        university = self.university_repo.get_university_details(university_id)
        return university
