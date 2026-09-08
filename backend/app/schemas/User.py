from pydantic import BaseModel,EmailStr
from typing import Optional

class UserResponse(BaseModel):
    id : int
    name : str
    email : EmailStr
    role : str
    
class UserUpdate(BaseModel):
    name : Optional[str]=None
    email : Optional[EmailStr]=None