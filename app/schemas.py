from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


# ---------- Request Schemas ----------

class UserCreate(BaseModel):
    """Schema for creating a new user."""
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    password: str


class UserUpdate(BaseModel):
    """Schema for updating an existing user."""
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    password: Optional[str] = None


# ---------- Response Schemas ----------

class UserResponse(BaseModel):
    """Schema for user response (excludes password)."""
    id: int
    username: str
    email: str
    full_name: Optional[str] = None
    avatar_url: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class UserListResponse(BaseModel):
    """Schema for paginated user list response."""
    total: int
    page: int
    per_page: int
    users: list[UserResponse]


class MessageResponse(BaseModel):
    """Schema for simple message response."""
    message: str


class FileUploadResponse(BaseModel):
    """Schema for file upload response."""
    filename: str
    url: str
    message: str
