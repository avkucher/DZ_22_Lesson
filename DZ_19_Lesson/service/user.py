from dao.user import UserDAO
import hashlib
import hmac
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self):
        return self.dao.get_all()

    def get_by_username(self, username):
        return self.dao.get_by_username(username)

    def create(self, user_new):
        user_new["password"] = self.get_user_password_hash(user_new.get("password"))
        return self.dao.create(user_new)

    def update(self, user_upd):
        user_upd["password"] = self.get_user_password_hash(user_upd.get("password"))
        self.dao.update(user_upd)
        return self.dao

    def delete(self, uid):
        self.dao.delete(uid)

    def get_user_password_hash(self, password):
        return hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ).decode('utf-8', 'ignore')

    def compare_passwords(self, password_hash, other_password) -> bool:
        return hmac.compare_digest(
            password_hash,
            hashlib.pbkdf2_hmac('sha256', other_password.encode(), PWD_HASH_SALT, PWD_HASH_ITERATIONS)
        )
