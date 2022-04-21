# здесь бизнес логика, в виде классов или методов. Cюда импортируются
# DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.

from dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, did):
        return self.dao.get_one(did)

    def get_all(self):
        return self.dao.get_all()

    def create(self, director_new):
        return self.dao.create(director_new)

    def update(self, director_new):
        self.dao.update(director_new)
        return self.dao

    def delete(self, did):
        self.dao.delete(did)

