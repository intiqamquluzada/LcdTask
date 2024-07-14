from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr

from pydantic import BaseModel

class PostCreate(BaseModel):
    text: str

class PostResponse(BaseModel):
    id: int
    text: str
    owner_id: int
