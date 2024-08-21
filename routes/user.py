from fastapi import APIRouter
from services.user import get_all_users

router = APIRouter()

@router.get("/users/all")
async def get_user():
    return get_all_users()