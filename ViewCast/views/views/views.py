from flask import Blueprint, render_template, redirect, request, flash, url_for, current_app
from werkzeug.utils import secure_filename
import os
from views.views.form.loginForm import LoginForm
from views.views.form.indexForm import IndexForm
from views.views.form.workstationForm import WorkstationForm

from ..services.usersService import UsersService

app = Blueprint("views", __name__, )
users_service = UsersService()
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


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


@app.route('/workstation/', methods=['GET', 'POST'])
def workstation():
    form = WorkstationForm()
    if request.method == 'POST':
        if 'media' not in request.files:
            return redirect(request.url)
        media = request.files['media']
        if media.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if media and allowed_file(media.filename):
            filename = secure_filename(media.filename)
            media.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

    return render_template("workstation.html", form=form)



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/a/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file', name=filename))
    return None
