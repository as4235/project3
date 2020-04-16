from flask_login import UserMixin
from sqlalchemy import Table, Column, Integer, String, MetaData

from . import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(64))


class record(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    name = db.Column(db.String(64))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User')
    numbers = db.Column(db.String(100))
    operation = db.Column(db.String(100))
    result = db.Column(db.Float(100))