# здесь модель SQLAlchemy для сущности, также могут быть
# дополнительные методы работы с моделью
# (но не с базой, с базой мы работаем в классе DAO)


from marshmallow import Schema, fields

from database import db


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class GenreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

