from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    drawings = db.relationship('Drawing')

class Drawing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

