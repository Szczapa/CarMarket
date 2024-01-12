import os
from fastapi.security import OAuth2PasswordBearer
from jwt import encode, decode, InvalidTokenError as PyJWTError


class JWTManager:
    SECRET_KEY = os.getenv("SECRET_JWT")
    if SECRET_KEY is None:
        raise ValueError("La clé secrète 'SECRET_JWT' est introuvable")
    ALGORITHM = os.getenv("JWT_ALGORITHM")
    if ALGORITHM is None:
        raise ValueError("L'algorithme 'JWT_ALGORITHM' est introuvable")

    @staticmethod
    def encodeJWT(data: dict) -> str:
        to_encode = data.copy()
        encoded_jwt = encode(to_encode, JWTManager.SECRET_KEY, algorithm=JWTManager.ALGORITHM)
        return encoded_jwt

    @staticmethod
    def decodeJWT(token: str):
        try:
            decode_token = decode(token, JWTManager.SECRET_KEY, algorithms=[JWTManager.ALGORITHM])
            return decode_token
        except PyJWTError:
            return None
