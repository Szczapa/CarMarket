from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from services.databaseManager import Base


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
    products = relationship("Product", back_populates="category_rel")

    def __repr__(self):
        return '<Category %r>' % (self.name)


class CategoryCreate(BaseModel):
    name: str
