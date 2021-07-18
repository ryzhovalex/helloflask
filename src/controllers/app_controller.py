import random
from flask import Flask
from ..models.app import App
from ..models.db import Database
from ..models.config import DevelopmentConfig
from ..views import home
from ..tests.cmds_test import add_test_user


# first and actually last creating a new instance of singleton class 'App'
app = App()
flask_app = app.get()
turbo = app.get_turbo()

# first and actually last creating a new instance of singleton class 'Database'
db = Database()


def create_app() -> Flask:
    """ Flask application factory. """
    # source: https://flask.palletsprojects.com/en/2.0.x/api/#flask.Config.from_object
    app.set_config(DevelopmentConfig)

    # chain database to app and make migrations
    db.init_app(app.get())
    db.migrate(app.get())

    # register blueprints for the app
    app.add_blueprint(home.bp)

    # chain shell commands to app 
    app.add_command(add_test_user)

    return app.get()
    

@flask_app.context_processor
def inject_cm0_data_dummy():
    """ Generate random dummy data and send it to Jinja scope for an operation turbo module. """
    values = {"temperature": random.uniform(18, 25), "humidity": random.uniform(20, 85), "pulse": random.uniform(70, 125)}
    return values


@flask_app.before_first_request
def launch_turbo_update_thread():
    app.start_turbo_thread()






