# coding=utf-8
import datetime

from application.extensions.database import database


class Results(database.Model):
    __tablename__ = 'results'

    result_id = database.Column('id', database.Integer, autoincrement=True, primary_key=True)
    title = database.Column(database.String(256))
    created_at = database.Column(database.DateTime, default=datetime.datetime.now)
