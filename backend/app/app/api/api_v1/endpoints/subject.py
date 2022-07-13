from typing import List

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from app import crud
from app.api import deps
from app import schemas, models

router = APIRouter()


@router.get("/", response_model=List[schemas.Subject])
def get_subjects(
        db: Session = Depends(deps.get_db),
        _: models.User = Depends(deps.get_current_active_user)
):
    subjects = crud.subject.get_multi(db)
    return subjects


@router.get("/details/", response_model=schemas.Subject)
def get_subject(
        id: str,
        db: Session = Depends(deps.get_db),
        _: models.User = Depends(deps.get_current_active_superuser)
):
    subject = crud.subject.get(db, id=id)
    return subject


@router.post("/", response_model=schemas.Subject)
def create_subject(
        *,
        db: Session = Depends(deps.get_db),
        obj_in: schemas.SubjectCreate,
        _: models.User = Depends(deps.get_current_active_superuser)
):
    subject = crud.subject.create(db, obj_in=obj_in)
    return subject


@router.put("/", response_model=schemas.Subject)
def update_subject(
        *,
        id: str,
        db: Session = Depends(deps.get_db),
        obj_in: schemas.SubjectUpdate,
        _: models.User = Depends(deps.get_current_active_superuser)
):
    db_obj = crud.subject.get(db, id)
    subject = crud.subject.update(db, db_obj=db_obj, obj_in=obj_in)
    return subject


@router.delete("/delete/", response_model=schemas.Subject)
def delete_subject(
        *,
        id: str,
        db: Session = Depends(deps.get_db),
        _: models.User = Depends(deps.get_current_active_superuser),
):
    subject = crud.subject.remove(db, id=id)
    return subject
