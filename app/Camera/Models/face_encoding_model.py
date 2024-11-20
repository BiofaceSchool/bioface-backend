from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.Camera.Enum.face_angle_enum import FaceAngleEnum
from config.database_config import Base
import json

class FaceEncoding(Base):
    __tablename__ = 'face_encodings'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    user_id: str = Column(String(length=36), ForeignKey('users.id'), nullable=False)
    angle: str = Column(String(length=50), nullable=False)
    encoding: str = Column(FaceAngleEnum, nullable=False) 

    user = relationship("User", back_populates="face_encodings")

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'angle': self.angle,
            'encoding': json.loads(self.encoding)  
        }

    class Config:
        from_attributes = True
