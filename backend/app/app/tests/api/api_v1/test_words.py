from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.word import create_random_word


def test_create_word(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    data = {
          "word": "string",
          "label": "string",
          "ipa": "string",
          "mean": "string",
          "cluster": "string",
          "source": "string",
          "lemma": "string",
          "position": "string",
          "frequency": "string1",
          "sample": [
            {
              "text": "string"
            }
          ]
        }
    response = client.post(
        f"{settings.API_V1_STR}/words/", headers=superuser_token_headers, json=data,
    )
    assert response.status_code == 200
    content = response.json()
    print(content)
    assert content["word"] == data["word"]
    assert content["label"] == data["label"]
    assert content["mean"] == data["mean"]
    assert content["cluster"] == data["cluster"]
    assert content["source"] == data["source"]
    assert content["lemma"] == data["lemma"]
    assert content["position"] == data["position"]
    assert content["frequency"] == data["frequency"]
    assert content["position"] == data["position"]
    assert len(content["sample"]) == len(data["sample"])


def test_read_word(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    word = create_random_word(db)
    response = client.get(
        f"{settings.API_V1_STR}/words/details/?id={word.id}", headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    print(content)
    assert content["word"] == word.word
    assert content["label"] == word.label
    assert content["mean"] == word.mean
    assert content["cluster"] == word.cluster
    assert content["source"] == word.source
    assert content["lemma"] == word.lemma
    assert content["position"] == word.position
    assert content["frequency"] == word.frequency
    assert content["position"] == word.position
    assert len(content["sample"]) == len(word.sample)


def test_update_word(
    client: TestClient, superuser_token_headers: dict, db: Session
):
    data = {
      "word": "update",
      "label": "update",
      "ipa": "update",
      "mean": "update",
      "cluster": "update",
      "source": "update",
      "lemma": "update",
      "frequency": "update",
      "position": "update"
    }

    word = create_random_word(db)
    response = client.put(
        f"{settings.API_V1_STR}/words/?id={word.id}",
        headers=superuser_token_headers,
        json=data
    )
    assert response.status_code == 200
    content = response.json()
    print(content)

    assert content["word"] == data["word"]
    assert content["label"] == data["label"]
    assert content["mean"] == data["mean"]
    assert content["cluster"] == data["cluster"]
    assert content["source"] == data["source"]
    assert content["lemma"] == data["lemma"]
    assert content["position"] == data["position"]
    assert content["frequency"] == data["frequency"]
    assert content["position"] == data["position"]
