import os
import time
import click
import random
import threading
from typing import Callable

from flask import Flask, Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy
from flask.cli import with_appcontext
from flask_migrate import Migrate
from turbo_flask import Turbo

from .config import Config
from ..tools.pathfinder import get_abs_path
from ..tools.singleton import Singleton


class App(metaclass=Singleton):
    """ Singleton Flask app class. """

    def __init__(self, template_path: str = "../templates/", static_path: str = "../static/"):
        template_abs_path = get_abs_path(template_path)
        static_abs_path = get_abs_path(static_path)
        self.app = Flask(__name__, template_folder=template_abs_path, static_folder=static_abs_path)

        # initialize turbo flask with our app
        # src: https://blog.miguelgrinberg.com/post/dynamically-update-your-flask-web-pages-using-turbo-flask
        self.turbo = Turbo(self.app)

    def get(self) -> Flask:
        return self.app
    
    def get_turbo(self) -> Turbo:
        return self.turbo

    def add_blueprint(self, blueprint: Blueprint) -> None:
        self.app.register_blueprint(blueprint)

    def set_config(self, config: Config) -> None:
        self.app.config.from_object(config)

    def add_command(self, command: Callable) -> None:
        self.app.cli.add_command(command)

    def start_turbo_thread(self) -> None:
        threading.Thread(target=self.update_turbo).start()

    def update_turbo(self):
        with self.app.app_context():
            while True:
                time.sleep(5)
                self.turbo.push(self.turbo.replace(render_template("turbo.html"), "turbo"))
