import random

from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload
from sqlalchemy.dialects.postgresql import insert


from .base import CRUDBase
from app.schemas.word import WordCreate, WordUpdate
from app.models.word import Word, LearnedWord
from app.models.sample import Sample


class CRUDWord(CRUDBase[Word, WordCreate, WordUpdate]):
    def create(self, db: Session, *, obj_in: WordCreate):
        obj_in_data = obj_in.dict()
        lst_sample = obj_in_data['sample']
        del obj_in_data['sample']

        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        if lst_sample is not None:
            for sample in lst_sample:
                word_id = db_obj.id
                q = insert(Sample).values(**sample, word_id=word_id)
                db.execute(q)
        db.commit()
        db.refresh(db_obj)
        return self.get_(db, id_=db_obj.id)

    def get_(self, db: Session, id_: int):
        q = select(Word).filter(Word.id == id_).options(selectinload(Word.sample))
        return db.execute(q).scalars().first()

    def get(self, db: Session, word_id: int, user_id: int):
        q = select(Word).filter(Word.id == word_id).options(selectinload(Word.sample))
        insert_stmt = insert(LearnedWord).values(
            word=word_id,
            user=user_id,
            mark_as_learned=False
        ).on_conflict_do_nothing(
            index_elements=['word', 'user']
        )
        db.execute(insert_stmt)
        db.commit()
        return db.execute(q).scalars().first()

    def get_learned_words(self, db: Session, user_id: int):
        q = select(LearnedWord.word).filter(LearnedWord.user == user_id)
        words_id = db.execute(q).scalars().all()
        w_q = select(Word).filter(Word.id.in_(words_id)).options(selectinload(Word.sample))
        words = db.execute(w_q).scalars().all()
        return words

    def practice_words(self, db: Session, user_id: int, max: int = 10):
        q = select(LearnedWord.word).filter(LearnedWord.user == user_id)
        words_id = db.execute(q).scalars().all()
        lst_id = random.choices(words_id, k=max)
        w_q = select(Word).filter(Word.id.in_(lst_id)).options(selectinload(Word.sample))
        words = db.execute(w_q).scalars().all()

        return words


word = CRUDWord(Word)
