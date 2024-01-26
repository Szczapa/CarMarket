from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from services.databaseManager import get_db
from services.loginManager import LoginManager as Lm

router = APIRouter()


@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # return await Lm.login(form_data,db)
    return Lm.login(form_data, db),
