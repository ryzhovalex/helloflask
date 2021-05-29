import os
import click
import random
from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
from flask.cli import with_appcontext
from flask_migrate import Migrate


db = SQLAlchemy()


def create_app():
    # proper init sequence from here: https://stackoverflow.com/a/20749534/14748231
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.abspath(os.getcwd()) + "/sqlite3.db" 
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

    db.init_app(app)

    # source: https://github.com/miguelgrinberg/flask-migrate
    migrate = Migrate(app, db)
    # if first time initialization:
    # -- $ flask db init
    # after each change at models:
    # -- $ flask db migrate
    # -- $ flask db upgrade

    app.cli.add_command(add_test_user)

    from .views import home
    app.register_blueprint(home.bp)

    from .models import User, Account, Order, Address

    return app


@click.command("add-test-user")
@with_appcontext
def add_test_user():
    from .models import User
    user = User(name=str(random.randint(-10**6, 10**6)), age=random.randint(5, 80))
    db.session.add(user)
    db.session.commit()
    click.echo("New test user added.")


