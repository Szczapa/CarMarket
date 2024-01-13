from services.databaseManager import Base
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel, Field
from typing import Optional


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    pseudo = Column(String(255), unique=True)
    first_name = Column(String(255), unique=True)
    last_name = Column(String(255), unique=True)
    password = Column(String(255), unique=True)
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

