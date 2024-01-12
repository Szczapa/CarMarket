from fastapi import APIRouter

router = APIRouter()


@router.get("/login")
async def login():
    return {"message": "Login"}


@router.get("/logout")
async def logout():
    return {"message": "Logout"}
