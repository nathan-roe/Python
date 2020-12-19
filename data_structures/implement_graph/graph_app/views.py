from django.shortcuts import render, HttpResponse, redirect
from .models import Person
def index(req):
    greg = Person(first_name="greg", last_name="gregory", connections=None)
    bob = Person(first_name="bob", last_name="dabuilder", connections=None)
    bob.addConnection(greg)
    print(greg.printConnections) 
    return render(req, "index.html")