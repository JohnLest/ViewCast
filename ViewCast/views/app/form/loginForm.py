from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, PasswordField, SubmitField


class LoginForm(FlaskForm):
    email = EmailField(label="Mail")
    psw = PasswordField(label="Password", )
    submit = SubmitField("Login")
