# coding=utf-8
from application.tasks.celery_tasks import get_html
import logging
logging.basicConfig()


def call_get_html(url):
    get_html.delay(url)
