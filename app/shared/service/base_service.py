from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
from typing import Type, TypeVar, Generic, List

T = TypeVar('T')  # Definimos un tipo genérico

class BaseService(Generic[T]):
    def __init__(self, db: Session):
        self.db = db

    def add_to_data_base(self, item: T) -> T:
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item

    def get_by_attribute(self, model_class: Type[T], attribute: str, value) -> T:
        result = self.db.query(model_class).filter(getattr(model_class, attribute) == value).first()
        if result is None:
            raise NoResultFound(f"No {model_class.__name__} found with {attribute}={value}")
        return result
    
    def update(self, item: T) -> T:
        self.db.commit()  # Asumiendo que el item ya tiene cambios
        return item

    def delete(self, model_class, item_id: int) -> None:
        item = self.get(model_class, item_id)
        if item:
            self.db.delete(item)
            self.db.commit()

    def find_all(self, model_class) -> List[T]:
        return self.db.query(model_class).all()
