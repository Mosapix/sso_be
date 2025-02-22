from fastapi import FastAPI

from app.presentation.v1.endpoints import auth

app = FastAPI(title="SSO Microservice")

app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])

@app.get("/")
async def root():
    return {"message": "OK"}