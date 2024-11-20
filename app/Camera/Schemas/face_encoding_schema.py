from pydantic import BaseModel

from app.Camera.Enum.face_angle_enum import FaceAngleEnum

class FaceEncodingRequest(BaseModel):
    user_id: str
    angle: FaceAngleEnum  
    encoding: str 
    
class FaceEncodingResponse(BaseModel):
    success: bool
    message: str

    class Config:
        orm_mode = True