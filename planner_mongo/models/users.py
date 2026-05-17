from beanie import Document

from pydantic import EmailStr, BaseModel
from pydantic_settings import BaseSettings

class User(Document):
    email: EmailStr
    password: str

    class Settings:
        name = "users"

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
            }
        }


class TokenResponse(BaseModel):
    access_token: str 
    token_type: str 
