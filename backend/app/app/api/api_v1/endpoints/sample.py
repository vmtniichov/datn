from typing import List

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException

from app import crud
from app.api import deps
from app import schemas, models

router = APIRouter()


@router.post("/", response_model=schemas.Sample)
def create_sample(
        *,
        db: Session = Depends(deps.get_db),
        obj_in: schemas.SampleCreate,
        _: models.User = Depends(deps.get_current_active_superuser)
):
    subject = crud.sample.create(db, obj_in=obj_in)
    return subject


@router.put("/", response_model=schemas.Sample)
def update_sample(
        *,
        id: int,
        db: Session = Depends(deps.get_db),
        obj_in: schemas.SampleUpdate,
        _: models.User = Depends(deps.get_current_active_superuser)
):
    db_obj = crud.sample.get(db, id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Not Found")
    sample = crud.sample.update(db, db_obj=db_obj, obj_in=obj_in)
    return sample


@router.delete("/delete/", response_model=schemas.Sample)
def delete_sample(
        *,
        id: int,
        db: Session = Depends(deps.get_db),
        _: models.User = Depends(deps.get_current_active_superuser),
):
    sample = crud.sample.remove(db, id=id)
    return sample
