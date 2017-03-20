# coding=utf-8
from flask import Blueprint


frontend_blueprint = Blueprint('frontend', __name__)


@frontend_blueprint.route('/')
def index():
    return 'hello world'
