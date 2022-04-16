from sqlalchemy import String, Boolean, Column, Integer

from app.db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(String, index=True, nullable=False, unique=True)
    full_name = Column(String)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
