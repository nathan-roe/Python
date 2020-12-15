from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User
import bcrypt
def logreg(req):
    return render(req, "logreg.html")
def register(req):
    hashed = bcrypt.hashpw('test'.encode(), bcrypt.gensalt()).decode()
    this_user = User.objects.create(
        first_name = req.POST["first_name"], 
        last_name = req.POST["last_name"], 
        email=req.POST["email"],
        password = hashed,
        confirm = hashed
    )
    req.session["uuid"] = this_user.id
    return redirect('/main')
def login(req):
    this_user = User.objects.filter(email = req.POST["email"])
    if this_user: 
        logged_user = this_user[0] 
        if bcrypt.checkpw(req.POST['password'].encode(), logged_user.password.encode()):
            req.session['uuid'] = logged_user.id
            return redirect('/success')
    return redirect("/")
def main(req):
    return render(req, "main.html")
