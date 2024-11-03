from datetime import datetime
from http import HTTPStatus
from fastapi import Request
import jwt
from app.Auth.Schemas.login_schema import TokenInfo
from app.Auth.auth_config import SECRET_JWT_KEY
from app.shared.Validator.error_factory import ValidationError

def validate_token_existence(token: str):
    if not token:
        raise ValidationError("Token is missing.", HTTPStatus.UNAUTHORIZED)

def validate_token_expiry(payload):
    if "exp" in payload:
        expiration_time = datetime.utcfromtimestamp(payload["exp"])
        if expiration_time < datetime.utcnow():
            raise ValidationError("Token has expired.", HTTPStatus.UNAUTHORIZED)

def validate_jwt_token(token: str):
    validate_token_existence(token)
    try:
        # Manejo de la decodificación del token.
        payload = jwt.decode(token, SECRET_JWT_KEY, algorithms=["HS256"], options={"verify_exp": False})
        validate_token_expiry(payload)
        return payload
    except jwt.ExpiredSignatureError:
        raise ValidationError("Token has expired.", HTTPStatus.UNAUTHORIZED)
    except jwt.DecodeError:
        raise ValidationError("Token is invalid.", HTTPStatus.UNAUTHORIZED)
    except jwt.InvalidTokenError:
        raise ValidationError("Token is invalid or malformed.", HTTPStatus.UNAUTHORIZED)  # Captura si el token no se puede decodificar.

def validate_cookie_token(request:Request ):
   token = request.cookies.get("access_token")
   if not token:
       raise ValidationError("cookie not found", HTTPStatus.UNAUTHORIZED)
   