from typing import List

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from app import crud
from app.api import deps
from app import schemas, models

router = APIRouter()


@router.get("/", response_model=List[schemas.UserCustomWord])
def get_words(
        db: Session = Depends(deps.get_db),
        _: models.User = Depends(deps.get_current_active_user),
):
    words = crud.user_word.get_multi(db)
    return words


@router.get("/details/", response_model=schemas.UserCustomWord)
def get_word(
        id: str, db: Session = Depends(deps.get_db),
        _: models.User = Depends(deps.get_current_active_user),
):
    word = crud.user_word.get(db, id=id)
    return word


@router.post("/", response_model=schemas.UserCustomWordCreate)
def create_word(
        *,
        db: Session = Depends(deps.get_db),
        obj_in: schemas.WordCreate,
        _: models.User = Depends(deps.get_current_active_user)
) -> models.Word:

    word = crud.user_word.create(db, obj_in=obj_in)
    return word


@router.put("/", response_model=schemas.UserCustomWordCreate)
def update_word(
        *,
        id: str,
        db: Session = Depends(deps.get_db),
        obj_in: schemas.WordUpdate,
        _: models.User = Depends(deps.get_current_active_user)
) -> models.Word:
    db_obj = crud.user_word.get_(db, id=id)
    word = crud.user_word.update(db, db_obj=db_obj, obj_in=obj_in)
    return word


@router.delete("/delete/", response_model=schemas.Word)
def delete_word(
        *,
        id: int,
        db: Session = Depends(deps.get_db),
        _: models.User = Depends(deps.get_current_active_user)
) -> models.Word:
    word = crud.user_word.remove(db, id=id)
    return word
