from backend.database.database import SessionLocal
from backend.database.models import UserHistory


def save_history(
    name,
    role,
    feature,
    input_text,
    output_text
):

    db = SessionLocal()

    try:

        entry = UserHistory(
            name=name,
            role=role,
            feature=feature,
            input_text=input_text,
            output_text=output_text
        )

        db.add(entry)

        db.commit()

    except Exception as e:

        db.rollback()

        print("Database Error:", e)

    finally:

        db.close()