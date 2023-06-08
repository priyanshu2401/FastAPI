from fastapi import FastAPI, HTTPException
from typing import List, Optional
from models import Gender, Role, User
from uuid import UUID, uuid4
 
app = FastAPI()

db: List[User] = [
    User(
        id = UUID("74ffdea1-cce2-4860-8aee-ba7a53efb504"),
        first_name = "Priyanshu",
        last_name = "Singh",
        gender = Gender.male,
        roles = [Role.student]
    ),
    User(
        id = UUID("de6f0cdb-98c5-4bc2-b035-9678fcca54a7"),
        first_name = "Aprajita",
        last_name = "Sinha",
        gender = Gender.female,
        roles = [Role.admin, Role.user]
    )
]

@app.get("/")
async def root():
    return {"hello":"world"}

@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
        raise HTTPException(
            status_code = 404,
            detail = f"user with id: {user_id} does not exist"
        )