from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from models.user import User
from services.jwtManager import JWTManager as JWTm
from services.securityManager import SecurityManager as Sm

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


class LoginManager:
    @staticmethod
    def login(form_login: OAuth2PasswordRequestForm, db: Session):
        # {
        #     "pseudo": "Eduardo",
        #     "mail": "Eduardo@gmail.com",
        #     "password": "Eduardo1234",
        #     "first_name": "Eduardo",
        #     "last_name": "Miguelito"
        # }
        form_mail = Sm.hash_mail(form_login.username)
        user = db.query(User).filter(User.hash_mail == form_mail).first()
        if not user:
            raise HTTPException(status_code=401, detail="No user found")
        if not Sm.verify_password(form_login.password, user.password):
            raise HTTPException(status_code=401, detail="Incorrect username or password")
        token = JWTm.encodeJWT(data={"sub": user.pseudo, "id": user.id, "mail": user.mail})
        return {"access_token": token, "token_type": "bearer"}


