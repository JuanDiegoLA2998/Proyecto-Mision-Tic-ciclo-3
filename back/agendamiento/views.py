from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from agendamiento.models import Profesional, Cita
from django.core.mail import EmailMessage 
from django.conf import settings

# Create your views here.


def show_home(request):
    return render(request, "index.html")


def signin(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/miscitas/")
        else:
            return HttpResponse("<h2>mal</h2>")

@login_required
def signout(request):
    logout(request)
    return redirect("/")



@login_required
def make_appointment(request):
    if request.method == "GET":
        profesionales = Profesional.objects.all()
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

        emailMess = EmailMessage(
            subject = "Tu cita ha sido agendada",
            body = f"Hemos agendado tu cita, Dr {profesional.nombre} te verá el día {fecha} a la siguiente hora: {hora}.",
            from_email = settings.EMAIL_HOST_USER,
            to  = [email],
            reply_to = [email]
        )
        emailMess.send()
        return redirect("/miscitas/")

@login_required
def next_appointment(request):
    next_appt=Cita.objects.filter(id_user=request.user.id).order_by('fecha').first()
    if next_appt is not None:
        return render(request, "micita.html", {"cita": next_appt})
    else:
        return render(request, "nocita.html")