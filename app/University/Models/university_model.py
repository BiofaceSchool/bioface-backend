# app/models/university.py
from sqlalchemy import Column, Integer, String
from app.Faculties.Models.faculty_model import Faculty
from config.database_config import Base
from ..config.university_constants import MAX_NAME_LENGTH, MAX_LOCATION_LENGTH, MAX_CONTACT_LENGTH
from sqlalchemy.orm import relationship

class University(Base):
    __tablename__ = 'universities'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(length=MAX_NAME_LENGTH), nullable=False)
    location = Column(String(length=MAX_LOCATION_LENGTH), nullable=False)
    contact = Column(String(length=MAX_CONTACT_LENGTH), nullable=False)

    campuses = relationship("Campus", back_populates="university")
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'contact': self.contact,
        }

    class Config:
        from_attributes = True

