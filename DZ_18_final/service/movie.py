# здесь бизнес логика, в виде классов или методов. Cюда импортируются
# DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.

from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all(self, qwery_user):
        if qwery_user.get("director_id") is not None:
            movies = self.dao.get_by_director_id(qwery_user.get("director_id"))
        elif qwery_user.get("genre_id") is not None:
            movies = self.dao.get_by_genre_id(qwery_user.get("genre_id"))
        elif qwery_user.get("year") is not None:
            movies = self.dao.get_by_year(qwery_user.get("year"))
        else:
            movies = self.dao.get_all()
        return movies


    def create(self, movie_new):
        return self.dao.create(movie_new)

    def update(self, movie_new):
        self.dao.update(movie_new)
        return self.dao

    def delete(self, mid):
        self.dao.delete(mid)

