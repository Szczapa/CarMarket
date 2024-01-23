from fastapi import FastAPI
from routers import login_router, product_router, user_router, category_router
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# origins = [
#     "http://localhost:3000",
# ]
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


@app.get("/")
async def root():
    return RedirectResponse("/docs")


app.include_router(login_router.router, tags=["login"])
app.include_router(product_router.router, tags=["product"])
app.include_router(user_router.router, tags=["user"])
app.include_router(category_router.router, tags=["category"])
