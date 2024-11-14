import re
from app.University.config.university_constants import MAX_NAME_LENGTH
from app.shared.Validator.error_factory import ValidationError

class FacultyValidator:

    @staticmethod
    def validate_name(name: str) -> str:
        if not name:
            raise ValidationError("Faculty name cannot be empty.")
        if len(name) < 3:
            raise ValidationError("Faculty name must be at least 3 characters long.")
        if len(name) > MAX_NAME_LENGTH:
            raise ValidationError(f"Faculty name must not exceed {MAX_NAME_LENGTH} characters.")
        if not re.match("^[A-Za-z\s]+$", name):
            raise ValidationError("Faculty name should only contain alphabetic characters and spaces.")
        return name
