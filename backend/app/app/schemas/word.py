import pydantic
from pydantic import BaseModel
from typing import List, Optional

from .sample import Sample, SampleCreate


class WordBase(BaseModel):
    word: str
    label: str
    ipa: Optional[str] = None
    mean: Optional[str] = None
    cluster: Optional[str] = None
    source: Optional[str] = None
    lemma: Optional[str] = None
    position: Optional[str] = None
    frequency: Optional[str] = None
    subject_id: Optional[str] = None

    class Config:
        arbitrary_types_allowed = True


class WordCreate(WordBase):
    sample: Optional[List[SampleCreate]]


class WordUpdate(BaseModel):
    word: Optional[str] = None
    label: Optional[str] = None
    ipa: Optional[str] = None
    mean: Optional[str] = None
    cluster: Optional[str] = None
    source: Optional[str] = None
    subject_id: Optional[str] = None
    lemma: Optional[str] = None
    frequency: Optional[str] = None
    position: Optional[str] = None


class Word(WordBase):
    id: int

    class Config:
        orm_mode = True


class WordWithSample(Word):
    sample: List[Sample]

    class Config:
        orm_mode = True


class UserCustomWordBase(BaseModel):
    word: str
    label: str
    ipa: Optional[str] = None
    mean: Optional[str] = None
    cluster: Optional[str] = None
    source: Optional[str] = None
    lemma: Optional[str] = None
    position: Optional[str] = None
    frequency: Optional[str] = None
    note: Optional[str] = None

class UserCustomWordCreate(UserCustomWordBase):
    pass

class UserCustomWordUpdate(UserCustomWordBase):
    pass


class UserCustomWord(UserCustomWordBase):
    id: int

    class Config:
        orm_mode = True