from typing import Optional
from pydantic import BaseModel, model_validator
from app.Camera.Enum.face_angle_enum import FaceAngleEnum
from app.Camera.Validator.face_encoding_validator import FaceReconitionValidator

    
from fastapi import UploadFile

class FacialDataRequest(BaseModel):
    user_id: int  # El ID del usuario al que pertenece la imagen
    landmarks: Optional[dict] = None  # Los landmarks faciales, opcional, ya que estos se generarán a partir de la imagen

    class Config:
        orm_mode = True