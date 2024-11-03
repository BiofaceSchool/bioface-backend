# app/Auth/Services/auth_service.py

import bcrypt
from fastapi import HTTPException, Request, Response
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm import Session
from app.Auth.Models.user_model import User
from app.Auth.Schemas.login_schema import LoginRequest, LoginResponse, TokenInfo
from app.Auth.Schemas.register_schema import RegisterRequest
from app.Auth.Validators.token_validators import validate_cookie_token
from app.Auth.Validators.user_validators import validate_all_user_fields, validate_login
from app.Auth.auth_config import SALT_ROUNDS
from app.Auth.Services.token_service import TokenService
from app.shared.service.base_service import BaseService

class AuthService(BaseService[User]):
    def __init__(self, db: Session):
        super().__init__(db)


    
    def login(self, request: LoginRequest):
        user = self.get_by_attribute(User, 'email', request.email)
        
        # Validate login credentials
        validate_login(user, request.password)

        # Create response with token set in cookie
        user_data = LoginResponse(id=user.id, email=user.email, role=user.role)
        return TokenService.create_token(user_data)


  
    
    def register(self, request: RegisterRequest):

        try:
            validate_all_user_fields(request, self.db)

            new_user = User(**request.dict())
            new_user.password = bcrypt.hashpw(request.password.encode('utf-8'), bcrypt.gensalt(SALT_ROUNDS))


            self.add_to_data_base(new_user) 

            token = TokenService.create_token(LoginResponse(**new_user.to_dict()))
            print(new_user.password)

            return token
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
        
    def logout(self, response: Response):
        try:            
            TokenService.remove_token_cookie(response)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))


    async def protect_user(self, request: Request):
        user = request.state.user
        user_info = TokenInfo(**user)
        
        return {"message": "You are authenticated", "user   ": user_info.email}
