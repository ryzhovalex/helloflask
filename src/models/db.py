""" SQLAlchemy database representasion """

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from ..tools.singleton import Singleton


class Database(metaclass=Singleton):
    """ Singleton database class."""

    def __init__(self):
        self.db = SQLAlchemy()

    def migrate(self, app):
        # source: https://github.com/miguelgrinberg/flask-migrate
        migrate = Migrate(app, self.db)

    def get(self):
        return self.db

    def init_app(self, app):
        self.db.init_app(app) 

    def add(self, entity):
        self.db.session.add(entity)

    def commit(self):
        self.db.session.commit()
