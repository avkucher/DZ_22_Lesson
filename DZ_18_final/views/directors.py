# здесь контроллеры/хендлеры/представления
# для обработки запросов (flask ручки).
# сюда импортируются сервисы из пакета service

from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema
from realisation import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        director_all = director_service.get_all()
        result = DirectorSchema(many=True).dump(director_all)
        return result, 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        qwery_one = director_service.get_one(did)
        result = DirectorSchema().dump(qwery_one)
        return result, 200

