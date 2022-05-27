from sqlalchemy.orm import Session

from .base import CRUDBase
from app.schemas.subject import SubjectCreate, SubjectUpdate
from app.models.subject import Subject


class CRUDSubject(CRUDBase[Subject, SubjectCreate, SubjectUpdate]):
    def create(self, db: Session, *, obj_in: SubjectCreate) -> Subject:
        obj_in_data = obj_in.dict()
        obj_in_data['id'] = "-".join(obj_in_data['name'].lower().split())
        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj



subject = CRUDSubject(Subject)
