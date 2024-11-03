from fastapi import APIRouter, Depends, Request, Response, status
from sqlalchemy.orm import Session

from app.Auth.Schemas.register_schema import RegisterRequest
from app.Auth.Schemas.login_schema import LoginRequest, TokenInfo
from app.Auth.Services.auth_service import AuthService
from config.dependency_config import get_db


auth = APIRouter()


@auth.post('/login', status_code=status.HTTP_200_OK,response_model = str)
async def login(request: LoginRequest, db: Session = Depends(get_db)):

    auth_service = AuthService(db)
    return auth_service.login(request)
    
  
    

@auth.post('/register', response_model=str)
def register(request: RegisterRequest, db: Session = Depends(get_db)):
    try:
        auth_service = AuthService(db)
        response = auth_service.register(request)
        return response
    except ConnectionError as e:
        raise ConnectionError(f"{e} Ocurrió un error en la conexión a la base de datos")

@auth.post('/logout')
async def logout( response: Response, db: Session = Depends(get_db)):
    auth_service = AuthService(db)
    auth_service.logout(response)  # Llama al método de logout
    return {"message": "Logged out successfully."}
    

@auth.post("/protected")
async def protectess(request: Request):
    user = request.state.user 
    user = TokenInfo(**user)

    return {"message": "You are authenticated", "user": user.email}

    