from app.db.base_class import Base

from sqlalchemy import String, ForeignKey, Integer
from sqlalchemy import Column


class Sample(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String, nullable=False)
    word_id = Column(Integer, ForeignKey("word.id"))
