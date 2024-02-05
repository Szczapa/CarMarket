from fastapi import APIRouter, Depends

from models.product import ProductCreate, ProductUpdate
from services.databaseManager import get_db
from services.productManager import ProductManager as Pm
from services.webhook import WebhookManager as Wm

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


@router.patch("/product/{product_id}")
async def update_product(product_id: int, update_data: ProductUpdate, db=Depends(get_db)):
    return Pm.updateProduct(product_id, update_data.model_dump(exclude_none=True), db)


@router.get("/products/sold")
async def get_sold_products(db=Depends(get_db)):
    return Pm.getSoldProducts(db)


@router.get("/products/{category_id}")
async def get_products_by_category(category_id: int, db=Depends(get_db)):
    return Pm.getProductsByCategory(category_id, db)


@router.post("/product/webhook")
async def webhook_product(data: dict):
    return Wm.productWebhook(data)


@router.delete("/product/{product_id}")
async def delete_product(product_id: int, db=Depends(get_db)):
    return Pm.deleteProduct(product_id, db)
