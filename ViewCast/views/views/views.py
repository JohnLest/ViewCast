from flask import Blueprint, render_template, redirect, request
from views.views.form.loginForm import LoginForm
from views.views.form.indexForm import IndexForm

from ..services.usersService import UsersService

app = Blueprint("views", __name__, )
users_service = UsersService()


@app.route("/", methods=["GET", "POST"])
def index():
    form = IndexForm()
    if request.method == "POST":
        if request.form.get("login"):
            return redirect("/login/")
    return render_template("index.html", form=form)


@app.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        user = users_service.connect(form.email.data.lower(), form.psw.data)
        if user is None: return render_template("login.html", form=form)
        return redirect("/workstation/")
    return render_template("login.html", form=form)


@app.route('/workstation/')
def workstation():
    return render_template("workstation.html")
