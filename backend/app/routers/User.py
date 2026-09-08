from fastapi import APIRouter,Depends,HTTPException
from app.database.database import Base,get_db
from app.models.UserModel import User
from app.schemas.User import UserResponse,UserUpdate
from sqlalchemy.orm import Session
from app.dependencies import get_current_user

router = APIRouter(prefix='/user',tags=["User"])

@router.get('/me',response_model=UserResponse)
def get_user(current_user:Session=Depends(get_current_user)):
    return current_user

@router.patch('/me')
def update_user(update_data:UserUpdate,current_user:User=Depends(get_current_user),db:Session=Depends(get_db)):
    update = update_data.model_dump(exclude_unset=True)
    
    for key,value in update.items():
        setattr(current_user,key,value)
        
    db.commit()
    db.refresh(current_user)
    
    return {
        "message" : "Details Updated Successfully"
    }
    
@router.delete('/me')
def delete_user(current_user:User=Depends(get_current_user),db:Session=Depends(get_db)):
    db.delete(current_user)
    db.commit()
    
    return {
        "message":"User Deleted Successfully"
    }