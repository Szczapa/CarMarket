import os

import bcrypt
from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()


class SecurityManager:
    key = os.getenv("SECRET_HASHER")
    if key is None:
        raise ValueError("La clé secrète 'SECRET_HASHER' est introuvable")

    sel_fix = os.getenv("SEL")
    if sel_fix is None:
        raise ValueError("Le sel_fix 'SEL' est introuvable")
    sel_fix = sel_fix.encode()
    key = key.encode()
    f = Fernet(key)

    @staticmethod
    def hash_password(password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    @staticmethod
    def verify_password(password, hashed_password):
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

    @staticmethod
    def hash_mail(mail):
        return bcrypt.hashpw(mail.encode('utf-8'), SecurityManager.sel_fix)

    @staticmethod
    def encrypt_data(data):
        encrypt = SecurityManager.f.encrypt(data.encode('utf-8'))
        return encrypt

    @staticmethod
    def decrypt_data(data):
        decrypt = SecurityManager.f.decrypt(data.encode('utf-8'))
        return decrypt
