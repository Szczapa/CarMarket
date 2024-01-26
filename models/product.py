from decimal import Decimal

from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Boolean, Numeric

from services.databaseManager import Base


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=False)
    description = Column(String(255), unique=False)
    price = Column(Numeric, unique=False)
    category = Column(Integer, unique=False)
    note = Column(Integer, unique=False, default=0)
    discount_amount = Column(Integer, unique=False, default=0)
    active_discount_price = Column(Boolean, unique=False, default=False)
    active_product = Column(Boolean, unique=False, default=True)

    def __repr__(self):
        return '<Product %r>' % (self.name)


class ProductCreate(BaseModel):
    name: str
    description: str
    price: Decimal
    category: int
