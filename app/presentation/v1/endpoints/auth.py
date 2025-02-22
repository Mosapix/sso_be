from fastapi import APIRouter, HTTPException, status

from app.domain.schemas.user import Token, UserLogin, UserCreate
from app.application.features.auth.command_service import AuthCommandService

router = APIRouter()

auth_command_service = AuthCommandService()

@router.post("/register", response_model=Token)
def register(request: UserCreate):
    result = auth_command_service.register(request)
    if result.status_code == status.HTTP_201_CREATED:
        return result.data
    return HTTPException(status_code=result.status_code, detail=result.message)

@router.post("/login", response_model=Token)
def login(request: UserLogin):
    result = auth_command_service.login(request)
    if result.status_code == status.HTTP_200_OK:
        return result.data
    return HTTPException(status_code=result.status_code, detail=result.message)