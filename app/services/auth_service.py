from sqlalchemy.orm import Session
from app.repositories.user_repo import get_user_by_username, create_user, get_all_users
from app.models.user import User
from app.core.security import hash_password, verify_password, create_access_token

def register_user(db: Session, username: str, email: str, password: str):
    user = User(
        username=username,
        email=email,
        hashed_password=hash_password(password)
    )
    return create_user(db, user)


def login_user(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)

    if not user or not verify_password(password, user.hashed_password):
        return None

    token = create_access_token({"sub": user.username})
    return token

def get_all_user(db: Session):
    all_users = get_all_users(db)
    return all_users