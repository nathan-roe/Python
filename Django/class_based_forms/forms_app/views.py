from django.shortcuts import render, redirect
from django.contrib import messages
from .components.form import RegisterForm as rf
# Create your views here.
def index(req):
    context = {"reg_form":rf}
    return render(req, "index.html", context)
def process(req):
    if req.method == "POST":
        showForm = rf(req.POST)
        if showForm.is_valid():
            return redirect("success")
        else:
            return redirect("index.html")