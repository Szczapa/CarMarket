from fastapi import APIRouter, Depends

from models.category import CategoryCreate
from services.categoryManager import CategoryManager as Cm
from services.databaseManager import get_db

router = APIRouter()


@router.get("/categories")
async def get_all_categories(db=Depends(get_db)):
    return Cm.getAllCategories(db)


@router.get("/category/{category_id}")
async def get_single_category(category_id: int, db=Depends(get_db)):
    return Cm.getCategory(category_id, db)


@router.post("/category")
async def create_category(category: CategoryCreate, db=Depends(get_db)):
    return Cm.addCategory(category, db)
