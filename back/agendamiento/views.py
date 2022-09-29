from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.

def show_home(request):
    return render(request, 'index.html')

def signin(request):
    if request.method == 'GET':
        print("estoy pasando por aqui")
        return render(request, 'login.html')
    else:
        print("cargando...")
        username=request.POST['email']
        password=request.POST['password']
        print(username, password)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return HttpResponse("<h2>bien</h2>")
        else:
            return HttpResponse("<h2>mal</h2>")

def make_appointment(request):
    return ""