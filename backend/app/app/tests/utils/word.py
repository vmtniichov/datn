from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.word import WordCreate
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_lower_string


def create_random_word(db: Session) -> models.Word:
    data = {
          "word": "string",
          "label": "string",
          "ipa": "string",
          "mean": "string",
          "cluster": "string",
          "source": "string",
          "lemma": "string",
          "position": "string",
          "frequency": "string",
          "sample": [
            {
              "text": "string"
            }
          ]
        }
    item_in = WordCreate(**data)
    return crud.word.create(db=db, obj_in=item_in)
