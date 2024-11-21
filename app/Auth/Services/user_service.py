from sqlalchemy.orm import Session
from app.Auth.Models.user_model import User
from app.Auth.Schemas.user_schema import UpdateUserSchema
from ..Repository.auth_repository import AuthRepository

class UserService():
    def __init__(self, db: Session):
        self.auth_repo = AuthRepository(db)
         
    def get_by_id(self, id: str):
        return self.auth_repo.get_user_by_id(id)
    
    def update_userdata(self, updated_user: UpdateUserSchema, user_id: str):
        user = self.auth_repo.update_user( updated_user, user_id)
        return user
    