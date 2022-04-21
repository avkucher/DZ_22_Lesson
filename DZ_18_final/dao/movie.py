# это файл для классов доступа к данным (Data Access Object).
# Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД

from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_all(self):
        return self.session.query(Movie).all()

    def get_by_director_id(self, did): # получение всех фильмов по директору
        return self.session.query(Movie).filter(Movie.director_id == did).all()

    def get_by_genre_id(self, gid):    # получение всех фильмов по жанру
        return self.session.query(Movie).filter(Movie.genre_id == gid).all()

    def get_by_year(self, yid):   # получение всех фильмов по году
        return self.session.query(Movie).filter(Movie.year == yid).all()

    # А еще можно сделать так, вместо всех методов get_by_*
    # t = self.session.query(Movie)
    # if "director_id" in filters:
    #     t = t.filter(Movie.director_id == filters.get("director_id"))
    # if "genre_id" in filters:
    #     t = t.filter(Movie.genre_id == filters.get("genre_id"))
    # if "year" in filters:
    #     t = t.filter(Movie.year == filters.get("year"))
    # return t.all()

    def create(self, movie_new):
        result = Movie(**movie_new)
        self.session.add(result)
        self.session.commit()
        return result

    def delete(self, mid):
        movie = self.get_one(mid)
        self.session.delete(movie)
        self.session.commit()

    def update(self, movie_mid):
        movie = self.get_one(movie_mid.get("id"))
        movie.title = movie_mid.get("title")
        movie.description = movie_mid.get("description")
        movie.trailer = movie_mid.get("trailer")
        movie.year = movie_mid.get("year")
        movie.rating = movie_mid.get("rating")
        movie.genre_id = movie_mid.get("genre_id")
        movie.director_id = movie_mid.get("director_id")

        self.session.add(movie)
        self.session.commit()
