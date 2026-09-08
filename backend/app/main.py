from fastapi import FastAPI
from app.models import UserModel
from app.database.database import Base,engine
from app.routers import Auth,User

UserModel.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(Auth.router)
app.include_router(User.router)

@app.get('/')
def root():
    return {"message":"Server Running Sucessfully"}