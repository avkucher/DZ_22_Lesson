# здесь бизнес логика, в виде классов или методов. Cюда импортируются
# DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.

from dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, gid):
        return self.dao.get_one(gid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, genre_new):
        return self.dao.create(genre_new)

    def update(self, genre_new):
        self.dao.update(genre_new)
        return self.dao

    def delete(self, gid):
        self.dao.delete(gid)

