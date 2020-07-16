from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "index.htm")

def create_users(request):
    errors = User.objects.validator(request.POST)
    #connects to models.py def validator through class User.objects
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user = User.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"])
        print(user)

        request.session['uid'] = user.id
        #request.session['greeting'] = request.POST["first_name"]

        return redirect("/dashboard")

def dashboard(request):
    context = {
        "logged_user": User.objects.get(id=request.session['uid']),
        "all_feels": Feels.objects.all().order_by("-created_at")
    }
    return render(request, "dashboard.htm", context)

def create_feels(request):
    Feels.objects.create(content=request.POST['content'], creator=User.objects.get(id=request.session['uid']))

    return redirect("/dashboard")

def create_like(request, feels_id):
    user = User.objects.get(id=request.session['uid'])
    feels = Feels.objects.get(id=feels_id)

    user.liked_feels.add(feels)

    return redirect("/dashboard")


