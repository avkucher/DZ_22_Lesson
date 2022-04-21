# здесь контроллеры/хендлеры/представления
# для обработки запросов (flask ручки).
# сюда импортируются сервисы из пакета service

from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from realisation import genre_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres_all = genre_service.get_all()
        result = GenreSchema(many=True).dump(genres_all)
        return result, 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        genre_one = genre_service.get_one(gid)
        result = GenreSchema().dump(genre_one)
        return result, 200