from typing import List

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException

from app import crud
from app.api import deps
from app import schemas, models

router = APIRouter()


@router.get("/", response_model=List[schemas.UserCustomWord])
def get_words(
        db: Session = Depends(deps.get_db),
        user: models.User = Depends(deps.get_current_active_user),
):
    words = crud.user_word.get_multi(db, user.id)
    return words


@router.get("/details/", response_model=schemas.UserCustomWord)
def get_word(
        id: int, db: Session = Depends(deps.get_db),
        user: models.User = Depends(deps.get_current_active_user),
):
    word = crud.user_word.get(db, id=id, user_id=user.id)
    if not word:
        raise HTTPException(
            status_code=404,
            detail="Not Found",
        )
    return word


@router.post("/", response_model=schemas.UserCustomWord)
def create_word(
        *,
        db: Session = Depends(deps.get_db),
        obj_in: schemas.UserCustomWordCreate,
        user: models.User = Depends(deps.get_current_active_user)
):
    obj_in.user_id = user.id
    word = crud.user_word.create(db, obj_in=obj_in)
    return word


@router.put("/", response_model=schemas.UserCustomWord)
def update_word(
        *,
        id: int,
        db: Session = Depends(deps.get_db),
        obj_in: schemas.UserCustomWordUpdate,
        user: models.User = Depends(deps.get_current_active_user)
):
    db_obj = crud.user_word.get(db, id=id, user_id=user.id)
    if db_obj:
        word = crud.user_word.update(db, db_obj=db_obj, obj_in=obj_in)
        return word
    raise HTTPException(
            status_code=404,
            detail="Not Found",
        )


@router.delete("/delete/", response_model=schemas.UserCustomWord)
def delete_word(
        *,
        id: int,
        db: Session = Depends(deps.get_db),
        user: models.User = Depends(deps.get_current_active_user)
):
    word = crud.user_word.get(db, id=id, user_id=user.id)
    if word:
        word = crud.user_word.remove(db, id=id)
        return word
    raise HTTPException(
            status_code=404,
            detail="Not Found",
        )
