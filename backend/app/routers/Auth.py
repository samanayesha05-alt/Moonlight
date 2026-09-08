from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.exc import IntegrityError
from app.database.database import Base,get_db
from app.models.UserModel import User
from app.schemas.Auth import UserCreate,UserResposne,UserLogin
from sqlalchemy.orm import Session
from app.core.security import hash_password,verify_password,create_access_token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix='/auth',tags=["Auth"])

@router.post('/register',response_model=UserResposne,status_code=201)
def create_user(userdata:UserCreate,db:Session=Depends(get_db)):
    user = User(
        name = userdata.name,
        email = userdata.email,
        password = hash_password(userdata.password),
        role = userdata.role
    )
    
    db.add(user)
    
    try :
        db.commit()
    except IntegrityError :
        db.rollback()
        raise HTTPException(status_code=409,detail="Email Already Exist")
    db.refresh(user)
    
    return user

@router.post('/login')
def get_user(form_data:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    db_user = db.query(User).filter(User.email==form_data.username).first()
    if not db_user or not verify_password(form_data.password,db_user.password):
        raise HTTPException(status_code=401,detail="Invalid Email or Password")
    
    data = {
        "sub" : str(db_user.id)
    }
    
    access_token = create_access_token(data)
    
    return {
        "message" : "Welcome Back🎉! Login Successful",
        "access_token" : access_token,
        "token_type" : "bearer"
    }