import datetime
from flask import request, abort, json
from dao.user import UserDAO
import hashlib
import hmac
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS, SECRET_KEY
import jwt


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def create_new_user(self, email, password):
        return self.dao.create(email=email, password=str(hash(password)))

    def check_auth(self, email, password):
        return str(hash(self.dao.get_by_email(email=email.password)) == str(hash(password)))

    def get_by_email(self, email):
        return self.dao.get_by_email(email=email)

    def get_by_id(self, id):
        return self.dao.get_by_id(id=id)

    def encode_auth_token(self, user_id):
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
                                        payload,
                                        "SECRET_KEY",
                                        algorithm="HS256").decode()
                    }


        except Exception as e:
            return e


    def decode_auth_token(self, auth_token):
        try:
            payload = jwt.decode(auth_token, 'SECRET_KEY')
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return "Signature expired. Please log in again."
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'


    # def get_one(self, uid):
    #     return self.dao.get_one(uid)
    #
    # def get_all(self):
    #     return self.dao.get_all()
    #
    # def get_by_username(self, username):
    #     return self.dao.get_by_username(username)
    #
    # def create(self, user_new):
    #     user_new["password"] = self.get_user_password_hash(user_new.get("password"))
    #     return self.dao.create(user_new)
    #
    # def update(self, user_upd):
    #     user_upd["password"] = self.get_user_password_hash(user_upd.get("password"))
    #     self.dao.update(user_upd)
    #     return self.dao
    #
    # def delete(self, uid):
    #     self.dao.delete(uid)
    #
    # def get_user_password_hash(self, password):
    #     return hashlib.pbkdf2_hmac(
    #         'sha256',
    #         password.encode('utf-8'),
    #         PWD_HASH_SALT,
    #         PWD_HASH_ITERATIONS
    #     ).decode('utf-8', 'ignore')
    #
    # def compare_passwords(self, password_hash, other_password) -> bool:
    #     return hmac.compare_digest(
    #         password_hash,
    #         hashlib.pbkdf2_hmac('sha256', other_password.encode(), PWD_HASH_SALT, PWD_HASH_ITERATIONS)
    #     )
