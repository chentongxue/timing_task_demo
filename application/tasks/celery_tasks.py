# coding=utf-8
import re

import requests
from application.extensions.flask_celery import celery
from application.models.results import Results
from application.extensions.database import database


@celery.task
def calc(a, b):
    return a + b


@celery.task
def get_html(url):
    regex = re.compile(r'<title>(.*?)</title>')
    response = requests.get(url)
    r = regex.findall(response.content)
    if r:
        result = Results()
        result.title = r[0]
        database.session.add(result)
        database.session.commit()
