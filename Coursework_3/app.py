from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.auth import auth_ns
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns
from views.user import user_ns




def create_app(config_object):

    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def create_data(app, db):
    with app.app_context():
        db.create_all()

        # u1 = User(email="vasya@mail.ru", password="my_little_pony", name="vasya",
        #           surname="Petrov", favorite_genre_id=1)
        # u2 = User(email="oleg@gmail.ru", password="qwerty", name="oleg",
        #           surname="Ivanov", favorite_genre_id=2)


        # with db.session.begin():
        #     db.session.add_all([u1, u2])


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)
    create_data(app, db)


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True, use_reloader=False)
