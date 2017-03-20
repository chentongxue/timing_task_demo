from flask import Flask
from application.extensions.scheduler import scheduler
from application.extensions.database import database
from application.views.frontend import frontend_blueprint
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore


def create_app(cfg):
    app = Flask(__name__)
    app.config.from_pyfile(cfg)
    configure_extensions(app)
    configure_blueprints(app)
    return app


def configure_extensions(app):
    app.config.update({'SCHEDULER_JOBSTORES': {
        'default': SQLAlchemyJobStore(url=app.config.get('SQLALCHEMY_DATABASE_URI')),
    }})
    database.init_app(app)
    scheduler.init_app(app)
    scheduler.start()


def configure_blueprints(app):
    app.register_blueprint(frontend_blueprint)
