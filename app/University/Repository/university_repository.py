from sqlalchemy.orm import Session

from app.Campus.Models.campus_model import Campus
from app.University.Models.university_model import University
from app.shared.Repository.base_repository import BaseRepository
from sqlalchemy.orm import joinedload

class UniversityRepository(BaseRepository[University]):
    def __init__(self, db: Session):
        super().__init__(db, University)

    def get_university_details(self, university_id: int):
        return (
            self.db.query(University)
            .options(
                joinedload(University.campuses).joinedload(Campus.faculties)
            )
            .filter(University.id == university_id)
            .first()
        )