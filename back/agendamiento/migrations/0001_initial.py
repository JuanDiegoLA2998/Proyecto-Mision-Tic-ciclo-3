# Generated by Django 4.1.1 on 2022-10-02 21:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profesional",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("nombre", models.TextField(max_length=100)),
                ("apellidos", models.TextField(max_length=100)),
                ("codigo_empleado", models.IntegerField()),
                ("facultad", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Appointment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("fecha", models.DateField()),
                ("hora", models.TimeField()),
                ("comentario", models.TextField(max_length=240)),
                ("email", models.TextField(max_length=100)),
                (
                    "id_profesional",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="agendamiento.profesional",
                    ),
                ),
                (
                    "id_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
