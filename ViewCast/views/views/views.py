from flask import Blueprint, render_template, redirect, request, flash, url_for, current_app
from werkzeug.utils import secure_filename
import os
from views.views.form.loginForm import LoginForm
from views.views.form.indexForm import IndexForm
from views.views.form.workstationForm import WorkstationForm

from ..services.usersService import UsersService
from ..services.mediaService import MediaService

app = Blueprint("views", __name__, )
users_service = UsersService()
media_service = MediaService()
ALLOWED_EXTENSIONS = media_service.get_media_type()
if len(ALLOWED_EXTENSIONS) < 1:
    current_app.logger.warning(f"No media extension find")


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
        if user is None:
            current_app.logger.warning(f"Error connection with {form.email.data.lower()}")
            return render_template("login.html", form=form)
        return redirect("/workstation/")
    return render_template("login.html", form=form)


@app.route('/workstation/', methods=['GET', 'POST'])
def workstation():
    form = WorkstationForm()
    if request.method == 'POST':
        current_app.logger.info(f"Add media")
        if 'media' not in request.files:
            return redirect(request.url)
        media = request.files['media']
        if media.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if media and allowed_file(media.filename):
            filename = secure_filename(media.filename)
            media.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            media_service.new_media(media.filename, filename.rsplit('.', 1)[1].lower(), 1)

    return render_template("workstation.html", form=form)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

