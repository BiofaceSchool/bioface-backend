from fastapi import APIRouter
from ..auth_config import TAG, ENDPOINT

auth = APIRouter()

auth.get("/")

auth.post( ENDPOINT + '/login'
          response_model=LoginResponse,
          , tags=TAG)
auth.post('/register', tags=TAG)
auth.post('/logout', tags=TAG)
auth.post('/protected', tags=TAG)