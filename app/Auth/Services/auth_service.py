# app/Auth/Services/auth_service.py

import bcrypt
from fastapi import HTTPException, Request, Response
from sqlalchemy.orm import Session
from app.Auth.Models.user_model import User
from app.Auth.Schemas.login_schema import LoginRequest, LoginResponse, TokenInfo
from app.Auth.Schemas.register_schema import RegisterRequest
from app.Auth.Schemas.user_schema import UpdateUserSchema, UserSchema
from app.Auth.Services.token_service import TokenService
from app.Auth.Validators.user_validators import validate_all_user_fields, validate_login
from app.Auth.auth_constants import SALT_ROUNDS
from ..Repository.auth_repository import AuthRepository

class AuthService():
    def __init__(self, db: Session):
        self.auth_repo = AuthRepository(db)
        
    def login(self, request: LoginRequest):

        user = self.auth_repo.get_by_email(request.email)
            
        # Validate login credentials
        validate_login(user, request.password)

        # Create response with token set in cookie
        user_data = LoginResponse(id=user.id, email=user.email, role=user.role)
        return TokenService.create_token(user_data)

    def register(self, request: RegisterRequest):
   
        validate_all_user_fields(request, self.auth_repo)

        new_user = User(**request.dict())
        new_user.password = bcrypt.hashpw(request.password.encode('utf-8'), bcrypt.gensalt(SALT_ROUNDS))
        
        self.auth_repo.add(new_user)

        token = TokenService.create_token(LoginResponse(**new_user.to_dict()))

        return token

        
    def logout(self, response: Response):
        try:            
            TokenService.remove_token_cookie(response)
        except HTTPException as e:
            raise e  
        except Exception as e:
            raise HTTPException(status_code=500, detail="Internal Server Error")

    async def protect_user(self, request: Request):
        user = request.state.user
        user_info = TokenInfo(**user)
        
        return {"message": "You are authenticated", "user   ": user_info.email}
    
    def get_by_id(self, id: str):
        return self.auth_repo.get_user_by_id(id)
    
    def update_user(self, updated_user: UpdateUserSchema, user_id: str):
        user = self.auth_repo.update_user(User(**updated_user.dict()), user_id)
        return user