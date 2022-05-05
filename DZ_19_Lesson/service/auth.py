import calendar
import datetime
import jwt
from constants import secret, algo
from service.user import UserService


class AuthService:

    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_tokens(self, username, password, is_refresh=False):
        user = self.user_service.get_by_username(username)

        if user is None:
            raise Exception()

        if not is_refresh:
            if not self.user_service.compare_passwords(user.password, password):
                raise Exception()

        data = {
            "username": user.username,
            "role": user.role
        }

        # 30 min access_token живет
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, secret, algorithm=algo)
        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, secret, algorithm=algo)
        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }

    def get_new_tokens(self, refresh_token: str):
        data = jwt.decode(jwt=refresh_token, key=secret, algorithms=algo)
        username = data.get("username")

        user = self.user_service.get_by_username(username=username)

        if user is None:
            raise Exception()
        return self.generate_tokens(username, user.password, is_refresh=True)
