from flask import Blueprint, render_template, redirect
from views.app.form.loginForm import LoginForm

from ..bll.usersService import UsersService

route = Blueprint("views", __name__, )
users_service = UsersService()

@route.route("/")
def hello_world():
    users = users_service.get_all_user()
    return render_template("index.html")


@route.route("/test/")
def test():
    return "test"


@route.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect("/")
    return render_template("login.html", form=form)
