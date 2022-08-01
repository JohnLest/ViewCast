from flask_wtf import FlaskForm
from wtforms import SubmitField


class IndexForm(FlaskForm):
    login = SubmitField("Login")
    subscribe = SubmitField("Subscribe")

