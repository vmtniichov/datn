from app.db.base_class import Base

from sqlalchemy import String, Integer, Column
from sqlalchemy.orm import relationship, backref
from .word import Word

class Subject(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

    words = relationship("Word", backref="subject")
