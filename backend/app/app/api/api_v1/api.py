from fastapi import APIRouter

from .endpoints import words, users, login, subject, user_words

api_router = APIRouter()
api_router.include_router(words.router, prefix="/words", tags=["words"])
api_router.include_router(words.router, prefix="/user_words", tags=["user_words"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(subject.router, prefix="/subject", tags=["subject"])
api_router.include_router(login.router, tags=["login"])
