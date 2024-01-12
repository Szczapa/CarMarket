import os

import bcrypt
from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()


class SecurityManager:
    key = os.getenv("SECRET_HASHER")
    if key is None:
        raise ValueError("La clé secrète 'SECRET_HASHER' est introuvable")
    key = key.encode()
    f = Fernet(key)

    @staticmethod
    def hash_password(password):
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    @staticmethod
    def verify_password(password, hashed_password):
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

    @staticmethod
    def encrypt_data(data):
        encrypt = SecurityManager.f.encrypt(data.lower().encode('utf-8'))
        return encrypt

    @staticmethod
    def decrypt_data(data):
        decrypt = SecurityManager.f.decrypt(data.lower().encode('utf-8'))
        return decrypt
