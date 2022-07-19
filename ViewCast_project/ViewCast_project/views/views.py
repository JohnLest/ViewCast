from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms.loginForm import LoginForm


def hello(request):
    return render(request,
                  "index.html")


def login(request):
    if len(request.POST) > 0:
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect("/")
        return render(request, "login.html", {"form": form})
    form = LoginForm()
    return render(request, "login.html", {"form": form})
