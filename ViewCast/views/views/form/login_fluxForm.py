from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, PasswordField, SubmitField
from wtforms import validators


class LoginFluxForm(FlaskForm):
    email = EmailField(label="Mail", validators=[validators.data_required("Mail obligatoire")])
    psw = PasswordField(label="Password", validators=[validators.data_required("password")])
    code = StringField(label="Broadcast code", validators=[validators.data_required('code')])
    submit = SubmitField("Connection")
