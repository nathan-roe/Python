from django.shortcuts import render
from .components.forms import RegisterForm
# Create your views here.
def index(req):
    return render(req, 'index.html')