from fastapi import APIRouter, Depends, HTTPException, Request, Response, status
from sqlalchemy.orm import Session

from app.Auth.Schemas.register_schema import RegisterRequest
from app.Auth.Schemas.login_schema import LoginRequest, TokenInfo
from app.Auth.Schemas.user_schema import UserSchema
from app.Auth.Services.auth_service import AuthService
from config.dependency_config import get_db


auth = APIRouter()

@auth.post('/login', status_code=status.HTTP_200_OK)
async def login(request: LoginRequest, db: Session = Depends(get_db)):
    try:
        auth_service = AuthService(db)
        return auth_service.login(request)
    except HTTPException as e:
        raise e
  

@auth.post('/register', status_code=status.HTTP_201_CREATED)
def register(request: RegisterRequest, db: Session = Depends(get_db)):
    auth_service = AuthService(db)
    response = auth_service.register(request)
    return response

  
@auth.post('/logout', status_code=status.HTTP_200_OK)
async def logout( response: Response, db: Session = Depends(get_db)):
    try :

        auth_service = AuthService(db)
        auth_service.logout(response)  # Llama al método de logout
        return {"message": "Logged out successfully."}
    except HTTPException as e:  
        raise e  
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
  
@auth.post("/protected", status_code=status.HTTP_200_OK)
async def protectess(request: Request):
    user = request.state.user 
    user = TokenInfo(**user)

    return {"message": "You are authenticated", "user": user.email}

@auth.get("/user/me", response_model=UserSchema)
async def get_my_info(request: Request, db: Session = Depends(get_db)):
    user = request.state.user 
    user = TokenInfo(**user)
    auth_service = AuthService(db)

    return auth_service.get_by_id(user.id)