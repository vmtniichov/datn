from sqlalchemy import update
from sqlalchemy.orm import Session

from .base import CRUDBase
from app.core.security import get_password_hash, verify_password
from app.schemas.user import UserCreate, UserUpdate, UserChangePassword
from app.models.user import User


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def get_by_email(self, db: Session, *, email: str):
        return db.query(User).filter(User.email == email).first()

    def create(self, db: Session, *, obj_in: UserCreate, super_user: bool = False) -> User:
        db_obj = User(
            student_id=obj_in.student_id,  # type: ignore
            email=obj_in.email,   # type: ignore
            hashed_password=get_password_hash(obj_in.password),    # type: ignore
            full_name=obj_in.full_name,    # type: ignore
            is_active=obj_in.is_active,  # type: ignore
            is_superuser=super_user  # type: ignore
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def authenticate(self, db: Session, *, email: str, password: str):
        user = self.get_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    def update(self, db: Session, id, obj_in: UserUpdate):
        q = update(User).where(User.id == id).values(full_name=obj_in.full_name)
        db.execute(q)
        return super().get(db, id=id)

    def change_password(self, db: Session, user, obj_in: UserChangePassword):
        if self.authenticate(db, email=user.email, password=obj_in.old_password):
            q = update(User).where(User.id == user.id).values(hashed_password=get_password_hash(obj_in.new_password))
            db.execute(q)
            db.commit()
            return super().get(db, id=user.id)

    def is_active(self, user: User) -> bool:
        return user.is_active

    def is_superuser(self, user: User) -> bool:
        return user.is_superuser


user = CRUDUser(User)
