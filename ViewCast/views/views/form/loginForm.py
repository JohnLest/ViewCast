from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, PasswordField, SubmitField
from wtforms import validators
from wtforms.validators import email_validator


class LoginForm(FlaskForm):
    email = EmailField(label="Mail", validators=[validators.data_required("Mail obligatoire")])
    psw = PasswordField(label="Password", validators=[validators.data_required("password")])
    submit = SubmitField("Login")
