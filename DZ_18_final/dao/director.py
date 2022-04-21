# это файл для классов доступа к данным (Data Access Object).
# Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД

from dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, did):
        return self.session.query(Director).get(did)

    def get_all(self):
        return self.session.query(Director).all()

    def create(self, director_new):
        dict_ = Director(**director_new)
        self.session.add(dict_)
        self.session.commit()
        return dict_

    def delete(self, did):
        director = self.get_one(did)
        self.session.delete(director)
        self.session.commit()

    def update(self, director_new):
        director = self.get_one(director_new.get("id"))
        director.name = director_new.get("name")
        self.session.add(director)
        self.session.commit()

