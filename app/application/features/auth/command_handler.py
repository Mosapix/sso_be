from datetime import timedelta
from http.client import HTTPException

from fastapi import status
from fastapi.security import HTTPAuthorizationCredentials

from app.application.response import Response
from app.core.security import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES, get_current_user
from app.domain.entities import User, UserProfile
from app.infrastructure.repositories import UserRepository, UserProfileRepository
from app.domain.schemas.user import UserCreate, UserLogin
from app.utils.hash import hash_password, verify_password
from app.domain.schemas.user import Token


class AuthCommandHandler:
    def __init__(self):
        self.user_repository = UserRepository()
        self.user_profile_repository = UserProfileRepository()

    def register(self, command: UserCreate) -> Response[Token | None]:
        existing_user = self.user_repository.get_by_email(email=command.email)
        if existing_user:
            return Response(
                status_code=status.HTTP_400_BAD_REQUEST,
                message="User with this email already exists",
                data=None
            )

        hashed_password = hash_password(str(command.password))
        new_user = User(
            username=command.username,
            email=command.email,
            hashed_password=hashed_password
        )
        self.user_repository.add(new_user)

        new_user_profile = UserProfile(
            user_id=new_user.id
        )
        self.user_profile_repository.add(new_user_profile)

        access_token = create_access_token(
            data={"sub": new_user.email},
            expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        )
        return Response(
            status_code=status.HTTP_201_CREATED,
            message="Successfully registered",
            data=Token(access_token=access_token, token_type="bearer")
        )

    def login(self, command: UserLogin) -> Response[Token | None]:
        user = self.user_repository.get_by_email(email=command.email)
        if not user or not verify_password(command.password, user.hashed_password):
            return Response(
                status_code=status.HTTP_400_BAD_REQUEST,
                message="Incorrect email or password",
                data=None
            )

        access_token = create_access_token(
            data={"sub": user.email},
            expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        )
        return Response(
            status_code=status.HTTP_200_OK,
            message="Successfully logged in",
            data=Token(access_token=access_token, token_type="bearer")
        )

    # def validate_token(self, token: str) -> Response:
    #     try:
    #         payload = get_current_user(HTTPAuthorizationCredentials(credentials=token, scheme="Bearer"))
    #         user = self.user_repository.get_by_email(payload["email"])
    #         return Response(
    #             status_code=status.HTTP_200_OK,
    #             message="Valid token",
    #             data={"valid": True, "user_id": user.id}
    #         )
    #     except HTTPException:
    #         return Response(
    #             status_code=status.HTTP_200_OK,
    #             message="Invalid token",
    #             data={"valid": False, "user_id": None}
    #         )
