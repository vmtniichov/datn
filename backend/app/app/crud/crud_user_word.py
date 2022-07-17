from sqlalchemy import select
from sqlalchemy.orm import Session
from .base import CRUDBase
from app.schemas.word import UserCustomWordCreate, UserCustomWordUpdate
from app.models.word import UserWord


class CRUDUserWord(CRUDBase[UserWord, UserCustomWordCreate, UserCustomWordUpdate]):
    def get(self, db: Session, id, user_id):
        q = select(UserWord).where(UserWord.id == id, UserWord.user_id == user_id)
        return db.execute(q).scalars().fisrt()

    def get_multi(self, db: Session, user_id):
        q = select(UserWord).where(UserWord.user_id == user_id)
        return db.execute(q).scalars().all()

user_word = CRUDUserWord(UserWord)
