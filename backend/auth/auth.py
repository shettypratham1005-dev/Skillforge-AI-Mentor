from backend.database.database import SessionLocal
from backend.database.models import User
from backend.auth.security import (
    hash_password,
    verify_password
)


def register_user(name, email, password):

    db = SessionLocal()

    existing = db.query(User).filter(
        User.email == email
    ).first()

    if existing:
        db.close()
        return False

    user = User(
        name=name,
        email=email,
        password=hash_password(password)
    )

    db.add(user)
    db.commit()
    db.close()

    return True


def login_user(email, password):

    db = SessionLocal()

    user = db.query(User).filter(
        User.email == email
    ).first()

    if not user:
        db.close()
        return None

    if verify_password(
        password,
        user.password
    ):
        db.close()
        return user

    db.close()
    return None