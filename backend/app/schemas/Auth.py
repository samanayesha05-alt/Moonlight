from pydantic import BaseModel,EmailStr

class UserCreate(BaseModel):
    name : str
    email : EmailStr
    password : str
    role : str
    
class UserLogin(BaseModel):
    email : EmailStr
    password : str
    
class UserResposne(BaseModel):
    id : int
    name : str
    email : EmailStr
    role : str