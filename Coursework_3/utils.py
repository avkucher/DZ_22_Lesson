import jwt
import datetime

from dao.model.user import User
from setup_db import db


def create_new_user(**kwargs):
    ent = User(**kwargs)
    with db.session.begin():
        db.session.add_all([ent])

    return ent

def encode_auth_token(user_id):
    try:
        payload = {
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=30),
            "iat": datetime.datetime.utcnow(),
            "sub": user_id
        }
        payload2 = {
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=30),
            "iat": datetime.datetime.utcnow(),
            "sub": user_id
        }
        return {"access_token":
                    jwt.encode(
                        payload,
                        "SECRET_KEY",
                        algorithm="HS256").decode(),
                "refresh_token":
                    jwt.encode(
                        payload2,
                        "SECRET_KEY",
                        algorithm="HS256").decode()
                }

    except Exception as e:
        return e
