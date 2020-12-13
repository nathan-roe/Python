from django.shortcuts import render, HttpResponse, redirect
def index(request):
    context = {
        "name": "Bob",
        "job": "Software Developer",
        "pets": ["Fred", "Greg", "Daniel", "John"]
    }
    return render(request, "index.html", context)
def second_page(request, str_val):
    return HttpResponse("This is the second page!")
def redirect_me(request):
    return redirect("/redirected_route")
def you_redirected(request):
    return HttpResponse("You redirected to me!")
def handlePost(request):
    request.session["first_name"] = request.POST["first_name"]
    request.session["last_name"] = request.POST["last_name"]
    request.session["password"] = request.POST["password"]
    return redirect("/success")
def success(request):
    return render(request, "success.html")