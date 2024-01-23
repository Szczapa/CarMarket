from services.databaseManager import Base
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)

    def __repr__(self):
        return '<Category %r>' % (self.name)


class CategoryCreate(BaseModel):
    name: str
