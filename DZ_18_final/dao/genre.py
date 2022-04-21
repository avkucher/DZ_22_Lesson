# это файл для классов доступа к данным (Data Access Object).
# Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД

from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, gid):
        return self.session.query(Genre).get(gid)

    def get_all(self):
        return self.session.query(Genre).all()

    def create(self, genre_new):
        dict_ = Genre(**genre_new)
        self.session.add(dict_)
        self.session.commit()
        return dict_

    def delete(self, gid):
        genre = self.get_one(gid)
        self.session.delete(genre)
        self.session.commit()

    def update(self, genre_new):
        genre = self.get_one(genre_new.get("id"))
        genre.name = genre_new.get("name")
        self.session.add(genre)
        self.session.commit()

