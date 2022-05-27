from app.db.base_class import Base

from sqlalchemy import String, Column
from sqlalchemy.orm import relationship, backref
from .word import Word

class Subject(Base):
    id = Column(String, primary_key=True)
    name = Column(String)
    description = Column(String, nullable=True)

    words = relationship("Word", backref="subject")
