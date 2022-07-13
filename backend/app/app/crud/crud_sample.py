from sqlalchemy.orm import Session

from .base import CRUDBase
from app.schemas.sample import SampleCreate, SampleUpdate
from app.models.sample import Sample


class CRUDSample(CRUDBase[Sample, SampleCreate, SampleUpdate]):
    pass


sample = CRUDSample(Sample)
