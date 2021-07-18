""" HelloFlask """

__author__ = "Alexander Ryzhov"
__email__ = "thed4rkof@gmail.com"
__version__ = "0.4.1-alpha.1"

import os
import sys
from src.controllers.app_controller import create_app # for being visible for the 'flask run' command
from src.errors.shell_errors import WrongSetupModeError, TooManySetupArgumentsError


APP_NAME = "HelloFlask"


def invoke_flask_init() -> None:
    os.system(f"{APP_NAME} (INFO) >>> Starting app initialization.")
    migrate_db()
    update_db()
    # TODO: here shell can return an error, so need to implement some error catching with subprocess module and redirect it to user in more convenient way


def migrate_db() -> None:
    os.system("python3 -m flask db migrate")


def update_db() -> None:
    os.system("python3 -m flask db update")


def run_flask(mode: str) -> None:
    """ Runs Flask app by sending system command depending on given mode. """
    if mode == "dev":
        os.system(f"{APP_NAME} (INFO) >>> Starting development server.")
        os.system("python3 -m flask run")
    elif mode == "prod":
        os.system(f"{APP_NAME} (INFO) >>> Starting production server.")
        os.system("python3 -m flask run --host=0.0.0.0 --port=5000")


def main() -> None:
    args = [x for x in sys.argv[1:]] # here we collect only 'useful' args with skipping first one with the script' name
    os.environ["FLASK_APP"] = __file__ # point to current file because we've imported an application factory

    """ NOTE: 
    Some systems can't properly locate flask and other python' packages, 
    so it's safe to use python' sys.path entries by running 'python3 -m flask ...'
    """
    if len(args) == 0:
        # no additional arguments, fast setup, using dev mode
        run_flask("dev")
    elif len(args) > 1:
        raise TooManySetupArgumentsError("Too many setup arguments.")
    elif args[0] == "dev" or args[0] == "prod":
        run_flask(args[0])
    elif args[0] == "init": # in dev init mode there is no need to setup static address
        invoke_flask_init()
    elif args[0] == "upd" or args[0] == "update": # perform fast accept (migrate+update) of newly made changes to orm models
        migrate_db()
        update_db()
    else:
        raise WrongSetupModeError("Unexpected mode: " + args[0])


##
if __name__ == "__main__":
    main()

