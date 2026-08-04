from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_pydantic_core_schema__(
            cls, _source_type, _handler
    ):
        from pydantic_core import core_schema
        return core_schema.any_schema()

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    name: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResetPassword(BaseModel):
    email: EmailStr
    new_password: str

class UserInDB(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    email: EmailStr
    hashed_password: str
    name: str

    model_config = {
        "populate_by_name": True,
        "arbitrary_types_allowed": True,
    }

class UserResponse(BaseModel):
    id: str
    email: EmailStr
    name: str

class Token(BaseModel):
    access_token: str
    token_type: str
