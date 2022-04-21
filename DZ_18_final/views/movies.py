# здесь контроллеры/хендлеры/представления
# для обработки запросов (flask ручки).
# сюда импортируются сервисы из пакета service

from flask import request
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
from realisation import movie_service

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        movies_all = movie_service.get_all()
        result = MovieSchema(many=True).dump(movies_all)
        return result, 200

    def get(self):
        director = request.args.get("director_id")
        genre = request.args.get("genre_id")
        year = request.args.get("year")
        filters = {
            "director_id": director,
            "genre_id": genre,
            "year": year,
        }
        all_movies = movie_service.get_all(filters)
        result = MovieSchema(many=True).dump(all_movies)
        return result, 200

    def post(self):
        request_json = request.json
        movie = movie_service.create(request_json)
        return "", 201, {"location": f"/movies/{movie.id}"}


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        query_mid = movie_service.get_one(mid)
        result = MovieSchema().dump(query_mid)
        return result, 200

    def put(self, mid):
        request_json = request.json
        if "id" not in request_json:
            request_json["id"] = mid
        movie_service.update(request_json)
        return "", 204

    def delete(self, mid):
        movie_service.delete(mid)
        return "", 204

