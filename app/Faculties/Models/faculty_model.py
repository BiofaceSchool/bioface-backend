# app/models/faculty.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.University.config.university_constants import MAX_NAME_LENGTH
from config.database_config import Base

class Faculty(Base):
    __tablename__ = 'faculties'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(length=MAX_NAME_LENGTH), nullable=False)
    campus_id = Column(Integer, ForeignKey('campuses.id'), nullable=False)
    
    campus = relationship("Campus", back_populates="faculties")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    class Config:
        from_attributes = True

