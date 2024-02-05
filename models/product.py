from decimal import Decimal

from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, Boolean, Numeric, ForeignKey
from sqlalchemy.orm import relationship

from services.databaseManager import Base


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))
    price = Column(Numeric)
    category_id = Column(Integer, ForeignKey('categories.id'))
    note = Column(Integer, default=0)
    discount_amount = Column(Integer, default=0)
    active_discount_price = Column(Boolean, default=False)
    active_product = Column(Boolean, default=True)

    # Ajoutez une relation ici
    category_rel = relationship("Category", back_populates="products")

    def __repr__(self):
        return '<Product %r>' % (self.name)


class ProductCreate(BaseModel):
    name: str
    description: str
    price: Decimal
    category: int


class ProductUpdate(BaseModel):
    discount_amount: float = None
    active_discount_price: bool = None
    active_product: bool = None
    note: int = None

