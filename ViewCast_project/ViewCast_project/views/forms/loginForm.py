from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label="Mail")
    psw = forms.CharField(label="Password", widget=forms.PasswordInput)
