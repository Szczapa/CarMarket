from fastapi import APIRouter, Depends
from models.category import CategoryCreate
from services.databaseManager import get_db
from services.categoryManager import CategoryManager as Cm
from models.product import ProductCreate

router = APIRouter()


@router.get("/categories")
async def get_all_categories(db=Depends(get_db)):
    return Cm.getAllCategories(db)


@router.get("/categories/{category_id}")
async def get_single_category(category_id: int, db=Depends(get_db)):
    return Cm.getCategory(category_id, db)


@router.post("/categories")
async def create_category(category: CategoryCreate, db=Depends(get_db)):
    return Cm.addCategory(category, db)
