# coding=utf-8
"""
worker start:
celery worker -A celery_worker.celery -l INFO
"""
from application.extensions.flask_celery import celery
from application import create_app

app = create_app('config.cfg')
app.app_context().push()

