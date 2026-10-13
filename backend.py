
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="User Management API")

# Temporary in-memory storage
users = {}
next_user_id = 1


# Request model
class UserCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: str


# Add a user
@app.post("/users", status_code=201)
def add_user(user: UserCreate):
    global next_user_id

    # Prevent duplicate email addresses
    for existing_user in users.values():
        if existing_user["email"] == user.email:
            raise HTTPException(
                status_code=409,
                detail="Email already exists"
            )

    new_user = {
        "id": next_user_id,
        "name": user.name,
        "email": user.email
    }

    users[next_user_id] = new_user
    next_user_id += 1

    return {
        "message": "User added successfully",
        "user": new_user
    }


# List all users
@app.get("/users")
def list_users():
    return {
        "count": len(users),
        "users": list(users.values())
    }


# Delete a user by ID
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    deleted_user = users.pop(user_id)

    return {
        "message": "User deleted successfully",
        "user": deleted_user
    }
