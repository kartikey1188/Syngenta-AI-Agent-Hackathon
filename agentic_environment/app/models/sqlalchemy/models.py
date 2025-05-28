from enum import Enum
from sqlalchemy import Column, Integer, String, Enum as SQLEnum
from . import Base, pwd_context     

class Role(Enum):
    GLOBAL_MANAGER = 'global_manager'
    PLANNING_MANAGER = 'planning_manager'
    FINANCE_MANAGER = 'finance_manager'

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    role = Column(SQLEnum(Role), nullable=False)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False, index=True)
    password_hash = Column(String(128), nullable=False)  # Storing hashed password

    def set_password(self, password: str):
        """Hash the password using passlib and store it."""
        self.password_hash = pwd_context.hash(password)

    def check_password(self, password: str) -> bool:
        """Verify password during login."""
        return pwd_context.verify(password, self.password_hash)
    
 

