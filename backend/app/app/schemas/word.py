import pydantic
from pydantic import BaseModel
from typing import List, Optional

from .sample import Sample, SampleCreate


class WordBase(BaseModel):
    word: str
    label: str
    ipa: str
    mean: str
    cluster: str
    source: str
    subject_id: int

    class Config:
        arbitrary_types_allowed = True


class WordCreate(WordBase):
    sample: Optional[List[SampleCreate]]


class WordUpdate(BaseModel):
    word: Optional[str]
    label: Optional[str]
    ipa: Optional[str]
    mean: Optional[str]
    cluster: Optional[str]
    source: Optional[str]
    subject_id: Optional[str]


class Word(WordBase):
    id: int

    class Config:
        orm_mode = True


class WordWithSample(Word):
    sample: List[Sample]

    class Config:
        orm_mode = True
