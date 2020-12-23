from django.shortcuts import render
from .components.forms import RegisterForm
# Create your views here.
def index(req):
    form = RegisterForm()
    context = {"reg_form": form}
    return render(req, 'index.html', context)
def process(req):
    if req.method = POST:
        bound_form = RegisterForm(req.POST)
    return redirect("index.html")