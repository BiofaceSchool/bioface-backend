from sqlalchemy.orm import Session

from app.Auth.Models.user_model import User
from app.shared.Repository.base_repository import BaseRepository


class AuthRepository(BaseRepository[User]):
    def __init__(self, db: Session):
        # Inicializamos con el modelo User
        super().__init__(db, User)

    def get_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()
    
    def get_user_by_id(self, id: str):
        try :
            result = self.db.query(User).get(id)
            self.validator.check_not_found(result, self.model_class.__name__, item_id=id)  # Using check_not_found here
            return result
        except Exception as e:
            self.validator.handle_error(e, 'retrieving', self.model_class.__name__, item_id=id)
        
    