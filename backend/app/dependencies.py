from fastapi.security import OAuth2PasswordBearer
from jose import jwt,JWTError
from app.core.config import settings
from fastapi import Depends,HTTPException
from app.database.database import get_db
from sqlalchemy.orm import Session
from app.models import UserModel

OAuth2scheme = OAuth2PasswordBearer(tokenUrl='auth/login')

credential_exception = HTTPException(status_code=401,detail="Could not validate credentials")

def get_current_user(token:str=Depends(OAuth2scheme),db:Session=Depends(get_db)):
    try :
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            settings.ALGORITHM
        )
        
        if payload is None:
            raise credential_exception
        
        user_id = payload.get("sub")
        
        db_user = db.query(UserModel.User).filter(UserModel.User.id==int(user_id)).first()
        
        if not db_user:
            raise credential_exception
        
        return db_user
          
    except JWTError:
        raise credential_exception