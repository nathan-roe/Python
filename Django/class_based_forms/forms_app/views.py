from django.shortcuts import render, redirect
from django.contrib import messages
from .components.form import RegisterForm as rf
from .models import User
# Create your views here.
def index(req):
    allUsers = User.objects.all()
    context = {"reg_form":rf, "users":allUsers}
    return render(req, "index.html", context)
def process(req):
    if req.method == "POST":
        showForm = rf(req.POST)
        if showForm.is_valid():
            this_user = User.objects.create(
                first_name=req.POST["first_name"],
                last_name=req.POST["last_name"],
                email=req.POST["email"],
                password=req.POST["password"],
                confirm_password=req.POST["confirm_password"]
            )
            this_user.save()
            req.session["uuid"] = this_user.id
            context = {
                "users":User.objects.all()
            }
            return render(req, "index.html", context)
        else:
            print("Something went wrong")
            return redirect("/")
def success(req):
    this_user = User.objects.get(id=req.session["uuid"])
    context = {"user":this_user}
    return render(req, "success.html", context)
        
