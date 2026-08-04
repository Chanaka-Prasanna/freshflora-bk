from fastapi import APIRouter, HTTPException, status
from app.models.user import UserCreate, UserLogin, UserResetPassword, UserInDB, Token
from app.core.security import get_password_hash, verify_password, create_access_token
from app.db.mongodb import db_client
from typing import Any

router = APIRouter()

@router.post("/signup", response_model=Token)
async def signup(user_in: UserCreate) -> Any:
    user = await db_client.db["users"].find_one({"email": user_in.email})
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system.",
        )
    
    hashed_password = get_password_hash(user_in.password)
    user_data = UserInDB(
        email=user_in.email,
        hashed_password=hashed_password,
        name=user_in.name
    )
    
    result = await db_client.db["users"].insert_one(user_data.model_dump(by_alias=True, exclude={"id"}))
    
    access_token = create_access_token(subject=str(result.inserted_id))
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/signin", response_model=Token)
async def signin(user_in: UserLogin) -> Any:
    user = await db_client.db["users"].find_one({"email": user_in.email})
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    
    if not verify_password(user_in.password, user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    
    access_token = create_access_token(subject=str(user["_id"]))
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/reset-password")
async def reset_password(user_in: UserResetPassword) -> Any:
    user = await db_client.db["users"].find_one({"email": user_in.email})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    hashed_password = get_password_hash(user_in.new_password)
    await db_client.db["users"].update_one(
        {"email": user_in.email},
        {"$set": {"hashed_password": hashed_password}}
    )
    return {"message": "Password updated successfully"}
