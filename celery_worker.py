# coding=utf-8
from application.extensions.flask_celery import celery
from application import create_app

app = create_app('config.cfg')
app.app_context().push()

