from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
def index(request):
    return render(request, "index.html")