from fastapi import APIRouter, HTTPException, status

from app.domain.schemas.user import Token, UserLogin, UserCreate
from app.application.features.auth.command_handler import AuthCommandHandler

router = APIRouter()

auth_command_handler = AuthCommandHandler()

@router.post("/register")
def register(request: UserCreate):
    result = auth_command_handler.register(request)
    if result.status_code == status.HTTP_201_CREATED:
        return result
    return HTTPException(status_code=result.status_code, detail=result.message)

@router.post("/login")
def login(request: UserLogin):
    result = auth_command_handler.login(request)
    if result.status_code == status.HTTP_200_OK:
        return result
    return HTTPException(status_code=result.status_code, detail=result.message)