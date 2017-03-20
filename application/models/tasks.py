# coding=utf-8
import datetime
from application.extensions.database import database


class Tasks(database.Model):
    __tablename__ = 'tasks'

    task_id = database.Column(database.Integer, autoincrement=True, primary_key=True)
    url = database.Column(database.String(256))
    status = database.Column(database.Boolean, default=0)
    created_at = database.Column(database.DateTime, default=datetime.datetime.now)
