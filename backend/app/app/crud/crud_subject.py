from sqlalchemy.orm import Session

from .base import CRUDBase
from app.schemas.subject import SubjectCreate, SubjectUpdate
from app.models.subject import Subject


class CRUDSubject(CRUDBase[Subject, SubjectCreate, SubjectUpdate]):
    pass


subject = CRUDSubject(Subject)
