from flask import (
    Blueprint, render_template, request, session, url_for
)


bp = Blueprint("home", __name__, url_prefix="/")


@bp.route("/")
def operation():
    return render_template("home.html")



