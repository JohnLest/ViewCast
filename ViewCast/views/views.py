from flask import Blueprint, render_template, redirect
from .form.loginForm import LoginForm

route = Blueprint("views", __name__, )


@route.route("/")
def hello_world():
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
