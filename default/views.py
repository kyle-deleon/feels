from django.shortcuts import render, redirect
from .models import User, Feels, Comments
# Create your views here.
def index(request):
    return render(request, "index.htm")

def create_users(request):
    User.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], user_name=request.POST["user_name"])

    return redirect("/dashboard")

def dashboard(request):
    return render(request, "dashboard.htm")