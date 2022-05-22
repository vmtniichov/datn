from typing import List

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException

from app import crud
from app.api import deps
from app import schemas, models

router = APIRouter()


@router.get("/", response_model=List[schemas.User])
def get_users(db: Session = Depends(deps.get_db), _=Depends(deps.get_current_active_superuser)):
    users = crud.user.get_multi(db)
    return users


@router.get("/me/", response_model=schemas.User)
def get_me(db: Session = Depends(deps.get_db),
             user=Depends(deps.get_current_active_user)):
    return user


@router.get("/details/", response_model=schemas.User)
def get_user(
        id: str,
        db: Session = Depends(deps.get_db),
        user=Depends(deps.get_current_active_superuser)):
    return crud.user.get(db, id=id)


@router.post("/", response_model=schemas.User)
def create_user(
    *,
    db: Session = Depends(deps.get_db),
    user_in: schemas.UserCreate,
):
    """
    Create new user.
    """
    user = crud.user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = crud.user.create(db, obj_in=user_in)
    return user


@router.put("/", response_model=schemas.User)
def update_user(
        *,
        db: Session = Depends(deps.get_db),
        obj_in: schemas.UserUpdate,
        current_user=Depends(deps.get_current_active_user)
) -> models.User:
    word = crud.user.update(db, db_obj=current_user, obj_in=obj_in)
    return word


@router.delete("/delete/", response_model=schemas.User)
def delete_user(
        *,
        student_id: int,
        db: Session = Depends(deps.get_db),
        _=Depends(deps.get_current_active_superuser)
) -> models.User:
    user = crud.user.remove(db, id=student_id)
    return user
