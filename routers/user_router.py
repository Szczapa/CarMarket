from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models.user import UserCreate
from services.databaseManager import get_db
from services.userManager import UserManager as Um

router = APIRouter()


@router.get('/users')
async def get_all_users(db: Session = Depends(get_db)):
    return Um.getAllUsers(db)


@router.get('/user/{user_id}')
async def get_single_user(user_id: int, db: Session = Depends(get_db)):
    return Um.getUserID(user_id, db)


@router.post('/user')
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return Um.createUser(user, db)


@router.delete('/user/{user_id}')
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    return Um.deleteUser(user_id, db)
