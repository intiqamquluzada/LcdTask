# controllers/auth_controller.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import user as user_schema
from app.services import auth_service
from app.utils.dependency import get_db
from app.models import user as user_model

router = APIRouter()

@router.post("/signup", response_model=user_schema.UserResponse)
def signup(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    hashed_password = auth_service.get_password_hash(user.password)
    db_user = user_model.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/login")
def login(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    db_user = auth_service.authenticate_user(db, user.email, user.password)
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = auth_service.create_access_token(data={"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}
