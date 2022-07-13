from pydantic import BaseModel
from typing import List, Optional



class SampleBase(BaseModel):
    text: str
    word_id: int
    mean: Optional[str] = None


class SampleCreate(BaseModel):
    text: str
    mean: Optional[str] = None


class SampleUpdate(BaseModel):
    text: str
    mean: Optional[str] = None


class Sample(SampleBase):
    id: int

    class Config:
        orm_mode = True