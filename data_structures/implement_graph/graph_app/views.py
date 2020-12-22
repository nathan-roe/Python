from django.shortcuts import render, HttpResponse, redirect
from .models import Person
def index(req):
    fred = Person.objects.create(first_name="fred", last_name="jones", connections=None)
    bob = Person.objects.create(first_name="bob", last_name="dabuilder", connections=fred)
    greg = Person.objects.create(first_name="greg", last_name="gregory", connections=bob)
    context = {
        "count": Person.findConnectionSpace(greg, bob)
    }
    return render(req, "index.html", context)
def process(req):
    
    return redirect("index.html")