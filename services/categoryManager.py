from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models.category import Category, CategoryCreate


class CategoryManager:
    @staticmethod
    def addCategory(form_data: CategoryCreate, db: Session):
        if db.query(Category).filter(Category.name == form_data.name).first():
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Category already exists")
        new_category = Category(
            name=form_data.name,
        )
        db.add(new_category)
        db.commit()
        db.refresh(new_category)
        return new_category

    @staticmethod
    def getAllCategories(db: Session):
        allCat = db.query(Category).all()
        if not allCat:
            raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="No Categories found")
        return allCat

    @staticmethod
    def getCategory(id_category, db: Session):
        category = db.query(Category).filter(Category.id == id_category).first()
        if category is None:
            raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Category not found")
        return category
