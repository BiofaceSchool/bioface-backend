from sqlalchemy import JSON, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from config.database_config import Base

class FacialData(Base):
    __tablename__ = "facial_data"
    
    id = Column(Integer, primary_key=True, index=True)  # ID único para cada dato facial
    user_id = Column(String(255), ForeignKey("users.id"), nullable=False)  # Relación con la tabla User
    
    # Solo se guardan los landmarks para la cara izquierda
    left_landmarks = Column(JSON, nullable=True)  # Landmarks para la cara izquierda
    
    # Relación con la tabla `User`
    user = relationship("User", back_populates="facial_data")
