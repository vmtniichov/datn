from app.db.base_class import Base

from sqlalchemy import String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column
from .sample import Sample


class LearnedWord(Base):
    word = Column(Integer, ForeignKey("word.id"), primary_key=True)
    user = Column(Integer, ForeignKey("user.id"), primary_key=True)
    mark_as_learned = Column(Boolean, nullable=True)


class Word(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    word = Column(String)
    label = Column(String)
    ipa = Column(String)
    mean = Column(String)
    cluster = Column(String)
    frequency = Column(String)
    lemma = Column(String)
    position = Column(String)
    source = Column(String)
    subject_id = Column(String, ForeignKey("subject.id"), nullable=True)

    sample = relationship("Sample", backref="word", cascade="all, delete-orphan")
    learned_users = relationship("User", secondary="learnedword", backref="learned_words")


class UserWord(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    word = Column(String)
    label = Column(String)
    ipa = Column(String)
    mean = Column(String)
    cluster = Column(String)
    frequency = Column(String)
    lemma = Column(String)
    position = Column(String)
    source = Column(String)
    note = Column(String)