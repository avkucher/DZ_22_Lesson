from flask import request, abort, json
from flask_restx import Resource, Namespace
import utils
# from implemented import auth_service
from implemented import user_service


auth_ns = Namespace('auth')


@auth_ns.route("/register")
class AuthView(Resource):

    def post(self):
        req_json = request.json
        password = str(req_json.get("password"))
        password_hash = user_service.make_user_password_hash(password)

        user = user_service.create_new_user(email=req_json.get("email"),
                                            password=password_hash)

        # token = user_service.encode_auth_token(user.email, str(user.password))

        return "Регистрация прошла успешно"  # json.dumps(token), 201


@auth_ns.route("/login")
class AuthView(Resource):
    def post(self):
        req_json = request.json
        user = user_service.get_by_email(email=req_json.get("email"))
        password = user.password
        new_password = str(req_json.get("password"))
        new_password_hash = user_service.make_user_password_hash(new_password)
        if password == new_password_hash:
            token = user_service.encode_auth_token(user.email, str(user.password))
            return json.dumps(token), 200

    def put(self):
        req_json = request.json
        token = req_json.get("refresh_token")

        tokens = user_service.approve_refresh_token(token)

        return tokens, 201









# @auth_ns.route('/')
# class AuthView(Resource):
#     def post(self):
#         req_json = request.json
#         username = req_json.get("username", None)
#         password = req_json.get("password", None)
#         if None in [username, password]:
#             return "", 400
#
#         tokens = auth_service.generate_tokens(username, password)
#
#         return tokens, 201
#
#     def put(self):
#         req_json = request.json
#         token = req_json.get("refresh_token")
#         tokens = auth_service.approve_refresh_token(token)
#         return tokens, 201





