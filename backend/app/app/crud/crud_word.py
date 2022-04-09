from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload
from sqlalchemy.dialects.postgresql import insert


from .base import CRUDBase
from app.schemas.word import WordCreate, WordUpdate
from app.models.word import Word
from app.models.sample import Sample


class CRUDWord(CRUDBase[Word, WordCreate, WordUpdate]):
    def create(self, db: Session, *, obj_in: WordCreate):
        obj_in_data = obj_in.dict()
        lst_sample = obj_in_data['sample']
        del obj_in_data['sample']

        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        word_id = db_obj.id
        for sample in lst_sample:
            q = insert(Sample).values(**sample, word_id=word_id)
            db.execute(q)
            db.commit()

        return db_obj

    def get(self, db: Session, id: int):
        q = select(Word).filter(Word.id == id).options(selectinload(Word.sample))
        return db.execute(q).scalars().first()


word = CRUDWord(Word)