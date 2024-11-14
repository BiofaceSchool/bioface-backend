# app/models/faculty.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.University.config.university_constants import MAX_NAME_LENGTH
from config.database_config import Base

class Campus(Base):
    __tablename__ = 'campuses'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(length=MAX_NAME_LENGTH), nullable=False)
    university_id = Column(Integer, ForeignKey('universities.id'), nullable=False)

    university = relationship("University", back_populates="campuses")
    faculties = relationship("Faculty", back_populates="campus")


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'university_id': self.university_id,
        }

    class Config:
        from_attributes = True

