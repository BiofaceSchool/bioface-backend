# app/Auth/Services/token_service.py

from fastapi import Request, Response
from fastapi.responses import JSONResponse

from datetime import datetime, timedelta

import jwt
from app.Auth.Schemas.login_schema import LoginResponse, TokenInfo
from ..auth_constants import SECRET_JWT_KEY

HOUR = 1000 * 60 * 60  

class TokenService:
    @staticmethod
    def create_token(user: LoginResponse) -> JSONResponse:
        payload = TokenInfo(
            email=user.email, id=user.id, role=user.role, exp=datetime.utcnow() + timedelta(hours=1)
        )
        
        token = jwt.encode(payload.dict(), SECRET_JWT_KEY, algorithm="HS256")
        
        # Prepare response with the user data and set cookie
        response = JSONResponse(content={"message": "Login successful"}) 
       
        TokenService.set_token_cookie(response, token)

        return response

    @staticmethod
    def set_token_cookie(response: Response, token: str):
        response.set_cookie(
            'access_token',
            token,
            httponly=True,
            secure=True,
            samesite='strict',
            max_age=HOUR
        )

    @staticmethod
    def remove_token_cookie(response: Response):
        response.delete_cookie('access_token')  # Esto debería funcionar correctamente
