from .base import CRUDBase
from app.schemas.word import UserCustomWordCreate, UserCustomWordUpdate
from app.models.word import UserWord


class CRUDUserWord(CRUDBase[UserWord, UserCustomWordCreate, UserCustomWordUpdate]):
    pass

user_word = CRUDUserWord(UserWord)
