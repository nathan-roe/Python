from django.shortcuts import render, HttpResponse, redirect
from .models import Person
def index(req):
    
    # bob = Person.objects.create(first_name="bob", last_name="dabuilder", connections=None)
    # fred = Person.objects.create(first_name="fred", last_name="jones", connections=bob)
    # greg = Person.objects.create(first_name="greg", last_name="gregory", connections=fred)
    # Person.printConnections(bob)
    # context = {
    #     "count": Person.findConnectionSpace(bob, greg)
    # }
    return render(req, "index.html")
def process(req):
    
    return redirect("index.html")