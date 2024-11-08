import re
import bcrypt
from http import HTTPStatus
from sqlalchemy.orm import Session

from app.Auth.Models.user_model import User
from app.Auth.Schemas.register_schema import RegisterRequest
from app.Auth.Schemas.user_schema import UserSchema
from app.shared.Validator.error_factory import ValidationError

def validate_all_user_fields(user: RegisterRequest, db: Session):
    validate_name(user.name)
    validate_name(user.lastname)
    validate_email(user.email, db)
    validate_password(user.password)
    validate_institution_name(user.institution_name)

def validate_login(user: UserSchema, password: str):
    validate_user_exists(user)
    validate_password_correct(password, user.password)


def validate_user_exists(user):
    if not user:
        raise ValidationError("User not found",HTTPStatus.NOT_FOUND)

def validate_password_correct(password: str, hashed_password: str):
    if not bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
        raise ValidationError("Wrong Password", HTTPStatus.BAD_REQUEST)

def validate_name(name: str):
    if not name or len(name) < 2:
        raise ValidationError("Name must have at least 2 characters.", HTTPStatus.BAD_REQUEST)

def validate_email(email: str, db: Session):
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(email_regex, email):
        raise ValidationError("Email must be a valid email address.", HTTPStatus.BAD_REQUEST)
    validate_email_not_taken(email, db)


def validate_password(password: str):
    if not isinstance(password, str):
        raise ValueError("Password must be a string.")

    if not any(char.isdigit() for char in password):
        raise ValueError("Password must contain at least one digit.")
    # Add other password validation checks as needed

    if len(password) < 8:
        raise ValidationError("Password must have at least 8 characters.", HTTPStatus.BAD_REQUEST)
    if not any(char.isdigit() for char in password):
        raise ValidationError("Password must have at least one number.", HTTPStatus.BAD_REQUEST)
    if not any(char.isupper() for char in password):
        raise ValidationError("Password must have at least one uppercase letter.", HTTPStatus.BAD_REQUEST)

def validate_institution_name(institution_name: str):
    if any(char.isdigit() for char in institution_name):
        raise ValidationError("Institution name must not contain numbers.", HTTPStatus.BAD_REQUEST)
    
    if not re.match(r'^[A-Za-z\s]+$', institution_name):
        raise ValidationError("Institution name must not contain special characters.", HTTPStatus.BAD_REQUEST)

def validate_email_not_taken(email: str, db: Session):
    existing_user = db.query(User).filter(User.email == email).first()
    if existing_user:
        raise ValidationError("Email already registered", HTTPStatus.BAD_REQUEST)