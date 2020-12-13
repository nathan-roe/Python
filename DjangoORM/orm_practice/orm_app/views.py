from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User, Pets
import bcrypt
def index(request):
    return render(request, "index.html")
def register(request):
    errors = User.objects.user_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/index")
    else:
        pw_hash = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], password=pw_hash, confirm=pw_hash)
        request.session["uuid"] = user.id
        return redirect("/success")
def login(request):
    user = User.objects.filter(email = request.POST["email"])
    if user: 
        if bcrypt.checkpw(request.POST['password'].encode(), user[0].password.encode()):
            request.session["uuid"] = user[0].id
            return redirect("/success")
    return redirect("/index")
def success(request):
    user = User.objects.get(id = request.session["uuid"])
    all_users = User.objects.all()
    context = {
        "user": user,
        "all_users": all_users
    }
    return render(request, "success.html", context)
def add_pet(request):
    Pets.objects.create(name=request.POST["name"], age=request.POST["age"], user=User.objects.get(id=request.session["uuid"]))
    return redirect("/success")

