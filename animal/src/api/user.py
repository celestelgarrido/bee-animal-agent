from fastapi import APIRouter, Depends
from animal.src.models.user import User

user = APIRouter()

@user.get("/users/{user_id}")
def read_user(user_id: int):
    print(user_id)
    return user_id


@user.get("/users")
def get_users():
    return [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]