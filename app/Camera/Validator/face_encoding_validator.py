import json
from typing import Any
from app.Camera.Enum.face_angle_enum import FaceAngleEnum
from app.shared.Validator.error_factory import ValidationError

class FaceReconitionValidator:
    @staticmethod
    def validate_face_encoding(encoding: str) -> bool:
        try:
            json.loads(encoding)
            return True
        except json.JSONDecodeError:
            raise ValidationError("JSON not valid")
    
    @staticmethod
    def validate_image(image: bytes) -> bool:
        if not image:
            raise ValidationError("The image is required")
        return True
    
    @staticmethod
    def validate_angle(angle: str) -> bool:
        if not isinstance(angle, FaceAngleEnum):
            raise ValidationError("The angle is required and must be a valid value from FaceAngleEnum (center, left, right)") 
        return True
