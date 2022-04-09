import pydantic
from pydantic import BaseModel
from typing import List, Optional



class SampleBase(BaseModel):
    text: str
    word_id: int


class SampleCreate(BaseModel):
    text: str


class SampleUpdate(BaseModel):
    pass


class Sample(SampleBase):
    id: int

    class Config:
        orm_mode = True