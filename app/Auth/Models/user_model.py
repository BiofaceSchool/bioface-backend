from datetime import datetime
import uuid
from sqlalchemy import Column, String, Enum
from sqlalchemy.orm import relationship
from ..Enum.user_role import UserRoleEnum
from ....config.database_config import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()), unique=True)
    name = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    institution_name = Column(String, nullable=False)
    profile_picture = Column(String, nullable=True)
    role = Column(Enum(UserRoleEnum), default=UserRoleEnum.STUDENT)


