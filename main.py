from fastapi import FastAPI
from routers import login_router, product_router
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get("/")
async def root():
    return RedirectResponse("/docs")


app.include_router(login_router.router, tags=["login"])
app.include_router(product_router.router, tags=["product"])
app.include_router(product_router.router, tags=["product"])
