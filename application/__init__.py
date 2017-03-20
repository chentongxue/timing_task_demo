from flask import Flask
from application.ext import scheduler
from application.views.frontend import frontend_blueprint


def create_app(cfg):
    app = Flask(__name__)
    app.config.from_pyfile(cfg)
    configure_extensions(app)
    configure_blueprints(app)
    return app


def configure_extensions(app):
    scheduler.init_app(app)


def configure_blueprints(app):
    app.register_blueprint(frontend_blueprint)
