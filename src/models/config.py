""" Configuration file
source: https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/
source2: https://flask.palletsprojects.com/en/2.0.x/config/
"""

import os


class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    DEBUG = False

    # postgresql connection works for connection to local psql (tested on UNIX system)
    # source: https://stackoverflow.com/questions/23839656/sqlalchemy-no-password-supplied-error
    SQLALCHEMY_DATABASE_URI = "postgresql:///mydb" 


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.abspath(os.getcwd()) + "/sqlite3.db" 


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
