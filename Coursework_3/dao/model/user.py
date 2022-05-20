from marshmallow import Schema, fields

from setup_db import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    password = db.Column(db.String, nullable=False)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    favorite_genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    favorite_genre = db.relationship("Genre")



class UserSchema(Schema):
    id = fields.Int()
    email = fields.Str()
    password = fields.Str()
    name = fields.Str()
    surname = fields.Str()

