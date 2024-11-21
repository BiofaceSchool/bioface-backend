from sqlalchemy.orm import Session

from app.Camera.Models.facial_data_model import FacialData
from app.shared.Repository.base_repository import BaseRepository


class FacialDataRepository(BaseRepository[FacialData]):
    def __init__(self, db: Session):
        super().__init__(db, FacialData)

    def get_facial_data_by_user_id(self, user_id: str):
        try:
            self.db.query(FacialData).filter(FacialData.user_id == user_id).first()
        except Exception as e:
            self.validator.handle_error(e, 'retrieving', self.model_class.__name__, item_id=user_id)
