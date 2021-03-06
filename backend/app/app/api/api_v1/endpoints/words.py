from typing import List

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from app import crud
from app.api import deps
from app import schemas, models

router = APIRouter()


@router.get("/", response_model=List[schemas.Word])
def get_words(
        db: Session = Depends(deps.get_db),
        _: models.User = Depends(deps.get_current_active_user),
):
    words = crud.word.get_multi(db)
    return words


@router.get("/details/", response_model=schemas.WordWithSample)
def get_word(
        id: str, db: Session = Depends(deps.get_db),
        user: models.User = Depends(deps.get_current_active_user),
):
    word = crud.word.get(db, word_id=id, user_id=user.id)
    return word


@router.post("/", response_model=schemas.WordWithSample)
def create_word(
        *,
        db: Session = Depends(deps.get_db),
        obj_in: schemas.WordCreate,
        _: models.User = Depends(deps.get_current_active_superuser)
) -> models.Word:

    word = crud.word.create(db, obj_in=obj_in)
    return word


@router.put("/", response_model=schemas.Word)
def update_word(
        *,
        id: str,
        db: Session = Depends(deps.get_db),
        obj_in: schemas.WordUpdate,
        _: models.User = Depends(deps.get_current_active_superuser)
) -> models.Word:
    db_obj = crud.word.get_(db, id_=id)
    word = crud.word.update(db, db_obj=db_obj, obj_in=obj_in)
    return word


@router.delete("/delete/", response_model=schemas.Word)
def delete_word(
        *,
        id: int,
        db: Session = Depends(deps.get_db),
        _: models.User = Depends(deps.get_current_active_superuser)
) -> models.Word:
    word = crud.word.remove(db, id=id)
    return word


@router.get("/learned_words/")
def get_learned_words(
        *,
        db: Session = Depends(deps.get_db),
        user: models.User = Depends(deps.get_current_active_user)
):
    words = crud.word.get_learned_words(db, user_id=user.id)
    return words


@router.get("/practice/")
def practice_words(
        *,
        db: Session = Depends(deps.get_db),
        _max: int = 10,
        user: models.User = Depends(deps.get_current_active_user)
):
    words = crud.word.practice_words(db, user_id=user.id, max=_max)
    return words
