from fastapi import APIRouter, Depends

from models.product import ProductCreate
from services.databaseManager import get_db
from services.productManager import ProductManager as Pm

router = APIRouter()


@router.post("/product")
async def create_product(product: ProductCreate, db=Depends(get_db)):
    return Pm.addProduct(product, db)


@router.get("/products/all")
async def get_all_products(db=Depends(get_db)):
    return Pm.getProducts(db)


@router.get("/products")
async def getActiveProduct(db=Depends(get_db)):
    return Pm.getProducts(db)


@router.get("/product/{product_id}")
async def get_single_product(product_id: int, db=Depends(get_db)):
    return Pm.getProduct(product_id, db)


@router.delete("/product/{product_id}")
async def delete_product(product_id: int, db=Depends(get_db)):
    return Pm.deleteProduct(product_id, db)


@router.put("/product/{product_id}")
async def update_product(product_id: int, db=Depends(get_db)):
    return Pm.updateProduct(product_id, db)


@router.get("/products/sold")
async def get_sold_products(db=Depends(get_db)):
    return Pm.getSoldProducts(db)


@router.get("/products/{category_id}")
async def get_products_by_category(category_id: int, db=Depends(get_db)):
    return Pm.getProductsByCategory(category_id, db)
