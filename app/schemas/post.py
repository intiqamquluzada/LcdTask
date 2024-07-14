from pydantic import BaseModel, Field
from typing import Optional

class PostBase(BaseModel):
    text: str = Field(..., max_length=1000)

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class PostResponse(PostBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
