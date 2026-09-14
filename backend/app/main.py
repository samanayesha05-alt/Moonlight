from fastapi import FastAPI
from app.models import UserModel
from app.database.database import Base,engine
from app.routers import Auth,User
from fastapi.middleware.cors import CORSMiddleware

UserModel.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(Auth.router)
app.include_router(User.router)

@app.get('/')
def root():
    return {"message":"Server Running Sucessfully"}