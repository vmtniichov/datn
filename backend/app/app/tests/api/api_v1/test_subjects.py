from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.word import create_random_word


def test_create_subject(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    data = {
      "name": "string"
    }
    response = client.post(
        f"{settings.API_V1_STR}/subject/", headers=superuser_token_headers, json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == data["name"]
    assert "id" in content


def test_read_subject(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    data = {
        "name": "string"
    }
    response = client.post(
        f"{settings.API_V1_STR}/subject/", headers=superuser_token_headers, json=data,
    )
    assert response.status_code == 200
    r = response.json()
    response = client.get(
        f"{settings.API_V1_STR}/subject/details/?id={r['id']}", headers=superuser_token_headers
    )

    content = response.json()
    print(content)
    print(data)
    assert content["name"] == data["name"]
    assert "id" in content
