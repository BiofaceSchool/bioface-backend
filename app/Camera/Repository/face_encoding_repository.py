from sqlalchemy.orm import Session

from app.Camera.Enum.face_angle_enum import FaceAngleEnum
from app.Camera.Models.face_encoding_model import FaceEncoding
from app.shared.Repository.base_repository import BaseRepository


class FaceEncodingRepository(BaseRepository[FaceEncoding]):
    def __init__(self, db: Session):
        super().__init__(db, FaceEncoding)

    def get_face_encoding(self, user_id: str, angle: FaceAngleEnum):
        try:
            enconde = self.db.query(FaceEncoding).filter(FaceEncoding.user_id == user_id, FaceEncoding.angle == angle).first()
            self.validator.check_not_found(enconde, self.model_class.__name__, item_id=user_id)
        except Exception as e:
            self.validator.handle_error(e, 'retrieving all', self.model_class.__name__)
