from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models.user import User, UserCreate
from services.securityManager import SecurityManager as Sm


class UserManager:
    @staticmethod
    def createUser(form_data: UserCreate, db: Session):
        hash_mail = Sm.hash_mail(form_data.mail)
        UserManager.checkEmail(hash_mail, db)
        lastname = Sm.encrypt_data(form_data.last_name)
        firstname = Sm.encrypt_data(form_data.first_name)
        mail = Sm.encrypt_data(form_data.mail)
        hashed_password = Sm.hash_password(form_data.password)
        pseudo = Sm.encrypt_data(form_data.pseudo)

        new_user = User(
            pseudo=pseudo,
            mail=mail,
            password=hashed_password,
            first_name=firstname,
            last_name=lastname,
            hash_mail=hash_mail
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    @staticmethod
    def deleteUser(user_id, db: Session):
        delete = db.query(User).filter(User.id == user_id).delete()
        if not delete:
            raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="User not found")
        return {"message": "User deleted"}

    @staticmethod
    def getAllUsers(db: Session):
        users = db.query(User).all()
        if not users:
            raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="No users found")
        users = [
            {
                "id": user.id,
                "pseudo": user.pseudo,
                "mail": user.mail,
                "first_name": user.first_name,
                "last_name": user.last_name,
            } for user in users
        ]
        return users

    @staticmethod
    def updateUser(db: Session):
        return print("updateUser")

    @staticmethod
    def getUserID(user_id, db: Session):
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="User not found")
        user_info = {
            "pseudo": Sm.decrypt_data(user.pseudo),
            "mail": Sm.decrypt_data(user.mail),
            "first_name": Sm.decrypt_data(user.first_name),
            "last_name": Sm.decrypt_data(user.last_name),
        }
        return user_info

    # Gestion de l'identité
    @staticmethod
    def getUserIdentity(db: Session):
        return print("getUserIdentity")

    @staticmethod
    def getUserLastname(db: Session):
        return print("getUserLastname")

    @staticmethod
    def getUserFirstname(db: Session):
        return print("getUserFirstname")

    # Gestion des adresses
    @staticmethod
    def getUserAddress(db: Session):
        return print("getUserAddress")

    @staticmethod
    def updateUserAddress(db: Session):
        return print("updateUserAddress")

    @staticmethod
    def deleteUserAddress(db: Session):
        return print("deleteUserAddress")

    # Gestion des numéros de téléphone
    @staticmethod
    def getUserPhone(db: Session):
        return print("getUserPhone")

    @staticmethod
    def updateUserPhone(db: Session):
        return print("updateUserPhone")

    # Gestion des emails
    @staticmethod
    def getUserEmail(db: Session):
        return print("getUserEmail")

    @staticmethod
    def checkEmail(hash_mail, db: Session):
        if db.query(User).filter(User.hash_mail == hash_mail).first():
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Mail already registered")
        return

    @staticmethod
    def updateUserEmail(db: Session):
        return print("updateUserEmail")

    # Gestion des mots de passe
    @staticmethod
    def getUserPassword(userid, db: Session):
        if db.query(User).filter(User.id == userid).first():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User not found")
        return print("getUserPassword")

    @staticmethod
    def updateUserPassword(db: Session):
        return print("updateUserPassword")

    # Gestion des rôles
    @staticmethod
    def getUserRole(db: Session):
        return print("getUserRole")

    @staticmethod
    def updateUserRole(db: Session):
        return print("updateUserRole")

    @staticmethod
    def deleteUserRole(db: Session):
        return print("deleteUserRole")

    @staticmethod
    def checkPseudo(pseudo, db: Session):
        return print("checkPseudo")
