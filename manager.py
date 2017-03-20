from flask_script import Manager

from application import create_app


app = create_app('config.cfg')
manager = Manager(app)


if __name__ == '__main__':
    manager.run()
