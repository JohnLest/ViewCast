from flask import Blueprint, render_template, redirect, request
from views.views.form.loginForm import LoginForm
from ..services.usersService import UsersService

route = Blueprint("views", __name__, )
users_service = UsersService()


@route.route("/")
def hello_world():
    return render_template("index.html")


@route.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        user = users_service.connect(form.email.data.lower(), form.psw.data)
        if user is None: return render_template("login.html", form=form)
        return redirect("/")
    return render_template("login.html", form=form)
