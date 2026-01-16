from fastapi import APIRouter
from api.auth import router as auth_router

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Welcome to the API"}

router.include_router(auth_router)