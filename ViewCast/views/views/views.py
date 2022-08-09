from flask import Blueprint, render_template, redirect, request, current_app, session

from werkzeug.utils import secure_filename
import os
from views.views.form.loginForm import LoginForm
from views.views.form.indexForm import IndexForm
from views.views.form.workstationForm import WorkstationForm
from views.views.form.login_fluxForm import LoginFluxForm

from ..services.usersService import UsersService
from ..services.mediaService import MediaService
from ..services.fluxService import FluxService

app = Blueprint("views", __name__, )
users_service = UsersService(current_app)
media_service = MediaService(current_app)
flux_service = FluxService(current_app)
ALLOWED_EXTENSIONS = media_service.get_media_type()
if len(ALLOWED_EXTENSIONS) < 1:
    current_app.logger.warning(f"No media extension find")


# region Route

@app.route("/", methods=["GET", "POST"])
def index():
    form = IndexForm()
    if request.method == "POST":
        if request.form.get("login"):
            return redirect("/login/")
        if request.form.get("watch"):
            return redirect('/watch/')
    return render_template("index.html", form=form)


@app.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        user = users_service.connect(form.email.data.lower(), form.psw.data)
        if user is None:
            current_app.logger.warning(f"Error connection with {form.email.data.lower()}")
            return render_template("login.html", form=form)
        session["name"] = user.name
        session["id_user"] = user.id_user
        return redirect("/workstation/")
    return render_template("login.html", form=form)


@app.route('/workstation/', methods=['GET', 'POST'])
def workstation():
    if not session.get("name"):
        current_app.logger.warning(f"User not connected")
        return redirect("/login/")
    form = WorkstationForm()
    if request.method == 'POST':
        request_form = check_form(request.form)
        if request_form == "new-media":
            add_media()
        elif request_form == "new-flux":
            add_flux(request.form)
    lst_media = media_service.get_list_medias_by_id_user(session.get("id_user"))
    matrice_media = [lst_media[_media:_media + 3] for _media in range(0, len(lst_media), 3)]
    if len(lst_media) < 0:
        current_app.logger.warning(f"No Media")
    return render_template("workstation.html", form=form, name=session.get("name"), table=matrice_media)


@app.route('/watch/', methods=['GET', 'POST'])
def watch():
    if not session.get("code"):
        form = LoginFluxForm()
        if request.method == "POST":
            user = users_service.connect(form.email.data.lower(), form.psw.data)
            if user is None:
                current_app.logger.warning(f"Error connection with {form.email.data.lower()}")
                return render_template("login_flux.html", form=form)
            session["name"] = user.name
            session["id_user"] = user.id_user
            session["code"] = form.code.data
        else:
            return render_template("login_flux.html", form=form)
    flux = flux_service.get_flux_by_url(session.get("code"))
    return render_template("flux.html", flux=flux)


# endregion

# region function
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def check_form(form):
    for key, val in form.items():
        if key == "form":
            return val


def add_media():
    current_app.logger.info(f"Add media")
    if 'media' not in request.files:
        return
    media = request.files['media']
    if media.filename == '':
        return
    if media and allowed_file(media.filename):
        filename = secure_filename(media.filename)
        media.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        _new_media = media_service.new_media(media.filename, filename.rsplit('.', 1)[1].lower(), 1)
        if _new_media is None:
            current_app.logger.warning(f"Error update with {filename}")


def add_flux(form):
    mutable_form = dict()
    mutable_form.update(form)
    mutable_form.pop("form")
    mutable_form.pop("next-in-txt")
    flux = []
    for key, val in mutable_form.items():
        detail_key = key.rsplit('-')
        data_flux = {"id_media": detail_key[0],
                     "position": detail_key[1],
                     "time": val}
        flux.append(data_flux)
    flux_service.create_new_flux(flux)
# endregion
