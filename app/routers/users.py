from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db import get_db
from app.schemas import UserCreate, UserUpdate, UserResponse, UserListResponse, MessageResponse
from app import crud

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/", response_model=UserListResponse)
def list_users(
    page: int = Query(1, ge=1, description="Page number"),
    per_page: int = Query(10, ge=1, le=100, description="Items per page"),
    db: Session = Depends(get_db),
):
    """Get all users with pagination."""
    users, total = crud.get_users(db, page=page, per_page=per_page)
    return UserListResponse(
        total=total,
        page=page,
        per_page=per_page,
        users=users,
    )


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """Get a single user by ID."""
    return crud.get_user_by_id(db, user_id)


@router.post("/", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """Create a new user."""
    return crud.create_user(db, user)


@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    """Update an existing user."""
    return crud.update_user(db, user_id, user)


@router.delete("/{user_id}", response_model=MessageResponse)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """Delete a user by ID."""
    crud.delete_user(db, user_id)
    return MessageResponse(message=f"User with id {user_id} deleted successfully")
