# Generated by Django 4.1.1 on 2022-10-02 21:39

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("agendamiento", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Appointment",
            new_name="Cita",
        ),
    ]
