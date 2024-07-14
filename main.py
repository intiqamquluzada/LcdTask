# main.py
from fastapi import FastAPI
from app.controllers import auth_controller, post_controller
from config import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_controller.router, prefix="/auth")
app.include_router(post_controller.router, prefix="/posts")


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application"}
