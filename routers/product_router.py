from fastapi import APIRouter, Depends
from services.loginManager import LoginManager as Lm
router = APIRouter()


@router.get("/products")
async def get_all_products():
    return {"message": "Products"}


@router.get("/products/{product_id}")
async def get_single_product(product_id: int):
    return {"message": f"Product {product_id}"}


@router.post("/products")
async def create_product():
    return {"message": "Create Product"}


@router.delete("/products/{product_id}")
async def delete_product(product_id: int):
    return {"message": f"Delete Product {product_id}"}


@router.put("/products/{product_id}")
async def update_product(product_id: int):
    return {"message": f"Update Product {product_id}"}
