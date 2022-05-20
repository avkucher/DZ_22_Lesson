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

        user = user_service.create_new_user(email=req_json.get("email"),
                                            password=str(hash(req_json.get("password"))))

        token = user_service.encode_auth_token(user.id)

        return json.dumps(token), 201


@auth_ns.route("/login")
class AuthView(Resource):
    def post(self):
        req_json = request.json
        user = user_service.get_by_email(email=req_json.get("email"))


        token = user_service.decode_auth_token(req_json.get("access_token").encode())

        result = int(token) == int(user.id)

        return json.dumps({"result": result}), 200








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





