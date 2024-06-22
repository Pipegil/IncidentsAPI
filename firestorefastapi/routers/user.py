from typing import List

from fastapi import APIRouter, Body, HTTPException, Depends
from pydantic.types import UUID4


from firestorefastapi.schemas.user import User, UserCreate, UserUpdate, UserLogin
from firestorefastapi.services.user import UserService

router = APIRouter()
user_service = UserService()


@router.post("/users", response_model=User, tags=["USERS"])
def create_user(user_create: UserCreate = Body(...)) -> User:
    return user_service.create_user(user_create)


@router.get("/users/{id}", response_model=User, tags=["USERS"])
def get_user(id: UUID4) -> User:
    user = user_service.get_user(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    return user


@router.get("/users", response_model=List[User], tags=["USERS"])
def list_users() -> List[User]:
    users = user_service.list_users()
    if not users:
        raise HTTPException(status_code=404, detail="Users not found.")
    return users


@router.put("/users/{id}", response_model=User, tags=["USERS"])
def update_user(id: UUID4, user_update: UserUpdate = Body(...)) -> User:
    user = user_service.get_user(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    return user_service.update_user(id, user_update)


@router.delete("/users/{id}", response_model=User, tags=["USERS"])
def delete_user(id: UUID4) -> User:
    user = user_service.get_user(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    return user_service.delete_user(id)


@router.post("/users/login", response_model=User, tags=["USERS"])
def login(user_login: UserLogin = Body(...)) -> User:
    return user_service.login(user_login)