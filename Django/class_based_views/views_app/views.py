from django.shortcuts import render, redirect
from django.views.generic import View

class Users(View):
    def get(self, request):
      # Get type view logic here!
      # (for REST this would be show all users)
        return render(request,'index.html')
    def post(self, request):
      # Post type view logic here!
      # (for REST this would be create a new user)
        return render(request,'index.html')