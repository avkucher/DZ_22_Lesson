from flask_restx import Namespace, Resource

from service.auth import AuthService
from Utils import auth_required, admin_required

protected_ns = Namespace('protected')

@protected_ns.route('/users')
class UsersView(Resource):
    @auth_required
    def get(self):
        return {}, 200


@protected_ns.route('/admin')
class AdminView(Resource):

    @admin_required
    def get(self):
        return {}, 200