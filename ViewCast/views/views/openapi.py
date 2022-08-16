from flask import Blueprint, render_template, redirect, request, current_app, session
from flask_openapi3 import OpenAPI, APIBlueprint, OAuthConfig
from flask_openapi3.models.security import OAuth2, OAuthFlows, OAuthFlowImplicit


from werkzeug.utils import secure_filename
import os
from views.views.form.loginForm import LoginForm
from views.views.form.indexForm import IndexForm
from views.views.form.workstationForm import WorkstationForm
from views.views.form.login_fluxForm import LoginFluxForm

from ..services.usersService import UsersService
from ..services.mediaService import MediaService
from ..services.fluxService import FluxService
from models.models.usersModel import UsersModel

app = APIBlueprint("api", __name__, url_prefix='/admin')
__users_service = UsersService(current_app)
__media_service = MediaService(current_app)
__flux_service = FluxService(current_app)

security = [
    {"oauth2": []}
]

@app.get("/users", responses={"200": UsersModel},  security=security)
def user():
    """
    get users
    """
    um= UsersModel(id=500,
                      company="coucou",
                      is_admin=False,
                      location="loc",
                      mail='a@a.a',
                      name="john",
                      password="psw",
                      path_media="/john")
    return um.json()