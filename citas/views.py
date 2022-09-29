from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.


def agendar_cita(request, id_prof, name):
    profesional = "No existe el profesional"
    for prof in profesionales:
        if prof[0] == id_prof:
            profesional = prof[1]
    return HttpResponse("<h1>Profesional seleccionado: %s</h1>" %(profesional))

