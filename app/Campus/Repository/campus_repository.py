
from app.Campus.Models.campus_model import Campus
from app.shared.Repository.base_repository import BaseRepository


class CampusRepository(BaseRepository[Campus]):
    def __init__(self, db):
        super().__init__(db, Campus)
