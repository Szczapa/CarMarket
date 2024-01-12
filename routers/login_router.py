from fastapi import APIRouter, Depends, HTTPException
from services.loginManager import LoginManager as Lm
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()


@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # return await Lm.login(form_data)
    return Lm.login(form_data),
