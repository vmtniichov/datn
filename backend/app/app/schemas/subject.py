from typing import  Optional
from pydantic import BaseModel


class SubjectBase(BaseModel):
    name: str
    description: Optional[str] = None


class SubjectCreate(SubjectBase):
    pass


class SubjectUpdate(SubjectBase):
    pass


class Subject(SubjectBase):
    id: str

    class Config:
        orm_mode = True
