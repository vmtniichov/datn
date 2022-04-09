from app.db.base_class import Base

from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column
from .sample import Sample


class Word(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    word = Column(String)
    label = Column(String)
    ipa = Column(String)
    mean = Column(String)
    cluster = Column(String)
    source = Column(String)
    subject_id = Column(Integer, ForeignKey("subject.id"))

    sample = relationship("Sample", backref="word", cascade="all, delete-orphan")

