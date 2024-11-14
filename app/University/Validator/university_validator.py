# app/validators/university_validator.py
import re
from app.shared.Validator.error_factory import ValidationError
from ..config.university_constants import MAX_NAME_LENGTH, MAX_LOCATION_LENGTH, MAX_CONTACT_LENGTH

class UniversityValidator:

    @staticmethod
    def validate_name(name: str) -> str:
        if not name:
            raise ValidationError("University name cannot be empty.")
        if len(name) < 3:
            raise ValidationError("University name must be at least 3 characters long.")
        if len(name) > MAX_NAME_LENGTH:
            raise ValidationError(f"University name must not exceed {MAX_NAME_LENGTH} characters.")
        if not re.match("^[A-Za-z\s]+$", name):
            raise ValidationError("University name should only contain alphabetic characters and spaces.")
        return name


    @staticmethod
    def validate_location(location: str) -> str:
        if not location:
            raise ValidationError("University location cannot be empty.")
        if len(location) < 3:
            raise ValidationError("University location must be at least 3 characters long.")
        if len(location) > MAX_LOCATION_LENGTH:
            raise ValidationError(f"University location must not exceed {MAX_LOCATION_LENGTH} characters.")
        return location
    
    @staticmethod
    def validate_contact(contact: str) -> str:
        if not contact:
            raise ValidationError("University contact cannot be empty.")
        if len(contact) < 5:
            raise ValidationError("University contact must be at least 5 characters long.")
        if len(contact) > MAX_CONTACT_LENGTH:
            raise ValidationError(f"University contact must not exceed {MAX_CONTACT_LENGTH} characters.")
        if not contact.replace(" ", "").isnumeric():
            raise ValidationError("University contact must be a valid numeric value.")
        return contact
