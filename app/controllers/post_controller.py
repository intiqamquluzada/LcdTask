from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas import post as post_schema
from app.utils.dependency import get_db, get_current_user
from app.services import post_service

router = APIRouter()

@router.post("/", response_model=post_schema.PostResponse)
def create_post(post: post_schema.PostCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return post_service.create_post(db=db, post=post, user_id=current_user.id)

@router.get("/", response_model=List[post_schema.PostResponse])
def read_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    posts = post_service.get_posts(db, user_id=current_user.id, skip=skip, limit=limit)
    return posts

@router.delete("/{post_id}", response_model=post_schema.PostResponse)
def delete_post(post_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return post_service.delete_post(db=db, post_id=post_id, user_id=current_user.id)
