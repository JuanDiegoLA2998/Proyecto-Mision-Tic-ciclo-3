from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from agendamiento.models import Profesional, Cita

# Create your views here.


def show_home(request):
    return render(request, "index.html")


def signin(request):
    if request.method == "GET":
        print("estoy pasando por aqui")
        return render(request, "login.html")
    else:
        print("cargando...")
        username = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/agendar/")
        else:
            return HttpResponse("<h2>mal</h2>")


def signout(request):
    return ""


@login_required
def make_appointment(request):
    if request.method == "GET":
        profesionales = Profesional.objects.all()
        print(profesionales)
        return render(request, "agendamiento.html", {"profesionales": profesionales})
    else:
        email = request.user.email
        userid = User.objects.get(username=request.user)
        profesional = Profesional.objects.get(id=request.POST["profesional"])
        fecha = request.POST["fecha"]
        hora = request.POST["appt-time"]
        comentario = request.POST["comentario"]
        new_appointment = Cita.objects.create(id_user=userid, fecha=fecha, hora=hora, comentario=comentario, email=email,id_profesional=profesional)
        new_appointment.save()
        return HttpResponse("<h1>se registro</h1>")