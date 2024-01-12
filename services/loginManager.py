from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from services.jwtManager import JWTManager as JWTm
from services.securityManager import SecurityManager as Sm

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


class LoginManager:
    @staticmethod
    def getCurrentUser(token: str = Depends(oauth2_scheme)) -> str:
        decoded_token = JWTm.decodeJWT(token)
        if not decoded_token:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")

        # Récupération de l'utilisateur
        user = "db.query(User).filter(User.id == decoded_token.get('id')).first()"
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    @staticmethod
    def login(form_data: OAuth2PasswordRequestForm):
        print(form_data)
        form_mail = form_data.username
        form_mail = Sm.encrypt_data(form_mail)

        # Récupération de l'utilisateur
        # user = "db.query(User).filter(User.mail == form_mail).first()"
        user = {
            "id": 1,
            "pseudo": "pseudo",
            "mail": "mail",
            "password": "password"
        }
        if not user:
            raise HTTPException(status_code=401, detail="incorrect username or password")

        # if not Sm.verify_password(form_data.password, user.password):
        #     raise HTTPException(status_code=401, detail="Incorrect username or password")
        if not form_data.password == user["password"]:
            raise HTTPException(status_code=401, detail="Incorrect username or password")

        # on crée le token
        # token = JWTm.encodeJWT(data={"sub": user.pseudo, "id": user.id, "mail": user.mail})
        token = JWTm.encodeJWT(data={"sub": user["pseudo"], "id": user["id"], "mail": user["mail"]})
        return {"access_token": token, "token_type": "bearer"}
