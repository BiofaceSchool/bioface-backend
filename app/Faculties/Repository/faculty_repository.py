
from app.Faculties.Models.faculty_model import Faculty
from app.University.Models.university_model import University
from app.shared.Repository.base_repository import BaseRepository
from app.University.Repository.university_repository import UniversityRepository

class FacultyRepository(BaseRepository[Faculty]):
    def __init__(self, db):
        super().__init__(db, Faculty)
