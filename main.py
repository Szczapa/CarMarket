from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import login_router, product_router, user_router, category_router

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://localhost:8000",
    # Ajoutez cette ligne si votre application Vue.js est servie à partir de 'http://localhost:8000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# @app.get("/")
# async def root():
#     return RedirectResponse("/docs")

@app.get("/")
def home():
    return "Hello, World!"


app.include_router(login_router.router, tags=["login"])
app.include_router(product_router.router, tags=["product"])
app.include_router(user_router.router, tags=["user"])
app.include_router(category_router.router, tags=["category"])
