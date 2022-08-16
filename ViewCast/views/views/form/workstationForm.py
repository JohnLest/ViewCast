from flask_wtf import FlaskForm
from wtforms import SubmitField, FileField


class WorkstationForm(FlaskForm):
    media = FileField("Media")
    upload = SubmitField("Upload")
