from fastapi import APIRouter, Depends
from services.loginManager import LoginManager as Lm
from fastapi.security import OAuth2PasswordRequestForm
from services.databaseManager import get_db
from sqlalchemy.orm import Session
router = APIRouter()


@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # return await Lm.login(form_data,db)
    return Lm.login(form_data, db),
