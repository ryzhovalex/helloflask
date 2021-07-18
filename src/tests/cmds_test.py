""" Script with CLI commands for test purposes """

import click
import random
from flask.cli import with_appcontext
from ..models.db import Database
from ..models.orm import User


db = Database()


@click.command("atu")
@with_appcontext
def add_test_user():
    user = User(name=str(random.randint(-10**6, 10**6)), age=random.randint(5, 80))
    db.add(user)
    db.commit()
    click.echo("New test user added.")
