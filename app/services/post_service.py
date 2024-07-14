from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models import post as post_model
from app.schemas import post as post_schema

def get_posts(db: Session, user_id: int, skip: int = 0, limit: int = 10):
    return db.query(post_model.Post).filter(post_model.Post.owner_id == user_id).offset(skip).limit(limit).all()

def create_post(db: Session, post: post_schema.PostCreate, user_id: int):
    db_post = post_model.Post(**post.dict(), owner_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def delete_post(db: Session, post_id: int, user_id: int):
    db_post = db.query(post_model.Post).filter(post_model.Post.id == post_id, post_model.Post.owner_id == user_id).first()
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    db.delete(db_post)
    db.commit()
    return db_post
