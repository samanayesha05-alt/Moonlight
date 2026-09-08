from jose import jwt 
from app.core.config import settings
from pwdlib import  PasswordHash
from datetime import datetime,timedelta,timezone

password_hash = PasswordHash.recommended()

def hash_password(password:str):
    return password_hash.hash(password)

def verify_password(plain_password:str,db_password:str):
    return password_hash.verify(plain_password,db_password)

def create_access_token(data:dict):
    payload = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(settings.ACCESS_TOKEN_EXPIRY_MINUTES) 
    
    payload["exp"] = expire
    
    encoded_jwt = jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )   
    
    return encoded_jwt
