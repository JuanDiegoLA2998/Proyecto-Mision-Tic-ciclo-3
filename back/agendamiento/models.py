from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profesional(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    nombre=models.TextField(max_length=100)
    apellidos=models.TextField(max_length=100)
    codigo_empleado=models.IntegerField()
    facultad=models.TextField()

    def __str__(self):
        return self.nombre

class Cita(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    id_profesional= models.ForeignKey(Profesional, on_delete=models.CASCADE)
    id_user= models.ForeignKey(User, on_delete=models.CASCADE)
    fecha= models.DateField()
    hora= models.TimeField()
    comentario= models.TextField(max_length=240)
    email= models.TextField(max_length=100)