# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.word import Word  # noqa
# from app.models.user import User  # noqa
