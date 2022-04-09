from typing import  Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    student_id: str
    email: str
    full_name: str
    password: str
    is_active: Optional[bool] = None


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    full_name: str
    hashed_password: str


class User(BaseModel):
    id: int
    student_id: str
    email: str
    full_name: str
    is_active: bool
    is_superuser: bool
    hashed_password: str

    class Config:
        orm_mode = True
