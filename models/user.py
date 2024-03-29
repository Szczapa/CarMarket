from pydantic import BaseModel
from sqlalchemy import Column, Integer, String

from services.databaseManager import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    pseudo = Column(String(255), unique=True)
    first_name = Column(String(255), unique=False)
    last_name = Column(String(255), unique=False)
    password = Column(String(255), unique=False)
    mail = Column(String(255), unique=True)
    hash_mail = Column(String(255), unique=True)

    def __repr__(self):
        return '<User %r>' % (self.pseudo)


class UserCreate(BaseModel):
    pseudo: str
    mail: str
    password: str
    first_name: str
    last_name: str
