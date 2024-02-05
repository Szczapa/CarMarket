from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models.category import Category
from models.product import Product, ProductCreate


class ProductManager:
    @staticmethod
    def addProduct(form_data: ProductCreate, db: Session):
        if db.query(Product).filter(Product.name == form_data.name).first():
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Product already exists")

        if db.query(Category).filter(Category.id == form_data.category).first() is None:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Category not exists")

        new_product = Product(
            name=form_data.name,
            description=form_data.description,
            price=form_data.price,
            category_id=form_data.category
        )
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
        return new_product

    @staticmethod
    def deleteProduct(product_id, db: Session):
        product = db.query(Product).filter(Product.id == product_id).first()
        if product is None:
            raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Product not found")
        db.delete(product)
        db.commit()
        return {"detail": "Product deleted"}

    @staticmethod
    def updateProduct(product_id, db: Session):
        product = db.query(Product).filter(Product.id == product_id).first()
        if product is None:
            raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Product not found")
        return

    @staticmethod
    def getProduct(id_product, db: Session):
        product = db.query(Product).filter(Product.id == id_product).first()
        if product is None:
            raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Product not found")
        return product

    @staticmethod
    def getProducts(db: Session):
        products = db.query(Product).all()
        if products is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Products not found")
        elif len(products) == 0:
            raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Products not found")
        return products

    @staticmethod
    def getActiveProduct(db: Session):
        products = db.query(Product).filter(Product.ative_product == True).all()
        if products is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Products not found")
        elif len(products) == 0:
            raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Products not found")
        return products

    @staticmethod
    def getActiveDiscountProducts(db: Session):
        products = db.query(Product).filter(Product.active_reduced_price == True, Product.ative_product == True).all()
        if products is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Products not found")
        elif len(products) == 0:
            raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Products not found")
        return products

    # Temporairy function
    @staticmethod
    def getProductsByCategory(category, db: Session):
        products = db.query(Product).filter(Product.category == category).all()
        if products is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Products not found")
        elif len(products) == 0:
            raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Products not found")

        return products

    @staticmethod
    def getActiveProductsByCategory(category, db: Session):
        products = db.query(Product).filter(Product.category == category, Product.ative_product == True).all()
        if products is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Products not found")
        elif len(products) == 0:
            raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Products not found")

        return products

    @staticmethod
    def GetProductsByNote(note, db: Session):
        products = db.query(Product).filter(Product.note == note).all()
        if products is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Products not found")
        elif len(products) == 0:
            raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Products not found")
        return products

    @staticmethod
    def getDiscountProducts(db: Session):
        products = db.query(Product).filter(Product.active_reduced_price == True).all()
        if products is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Products not found")
        elif len(products) == 0:
            raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Products not found")
        return products

    @staticmethod
    def updateProduct(product_id, update_data, db: Session):
        product = db.query(Product).filter(Product.id == product_id).first()
        if product is None:
            raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Product not found")
        for key, value in update_data.items():
            setattr(product, key, value)
        db.commit()
        db.refresh(product)
        return product
