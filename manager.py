from flask_script import Manager

from application import create_app
from application.extensions.database import database


app = create_app('config.cfg')
manager = Manager(app)


@manager.command
def create_database():
    database.create_all()


if __name__ == '__main__':
    manager.run()
