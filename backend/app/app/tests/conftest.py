from typing import Dict, Generator

import pytest
from fastapi import Header
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.session import SessionLocal
from app.main import app
from app.api.deps import verify_administrator
from app.tests.utils.user import authentication_token_from_email
from app.tests.utils.utils import get_superuser_token_headers


@pytest.fixture(scope="session")
def db() -> Generator:
    yield SessionLocal()


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="module")
def superuser_token_headers(client: TestClient) -> Dict[str, str]:
    return get_superuser_token_headers(client)


@pytest.fixture(scope="module")
def normal_user_token_headers(client: TestClient, db: Session) -> Dict[str, str]:
    return authentication_token_from_email(
        client=client, email=settings.FIRST_SUPERUSER, db=db
    )


@pytest.fixture
def admin():
    return {
        "authorization": f"Basic {settings.FIRST_SUPERUSER}"
    }


def auth(authorization: str = Header(None)):
    _, username = authorization.split()
    return {'username': username}


@pytest.fixture(autouse=True)
def auth_override():
    app.dependency_overrides[verify_administrator] = auth
    yield app
    app.dependency_overrides = {}
