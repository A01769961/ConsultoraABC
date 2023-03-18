from django.db import models
from shortuuid.django_fields import ShortUUIDField

# Create your models here.
class usuario(models.Model):
    ShortUUIDField(
        length=8,
        max_length=8,
        prefix="id_",
        primary_key=True,
    )
    name = models.CharField(max_length=40)
    PlastName = models.CharField(max_length=40)
    MLastName = models.CharField(max_length=40)
    mail = models.CharField(max_length=20)
    contrasenia = models.CharField(max_length=16)
    rol = models.CharField(max_length=3)

class consultor(models.Model):
    id = ShortUUIDField(
        length=8,
        max_length=8,
        prefix="id_",
        primary_key=True,
    )
    id_proyecto = models.IntegerField()
    status = models.CharField(max_length=5)

class proyecto(models.Model):
    id = ShortUUIDField(
        length=8,
        max_length=8,
        prefix="id_",
        primary_key=True,
    )
    id_administrador = models.IntegerField()
    id_cliente = models.IntegerField()

class reportes(models.Model):
    id = ShortUUIDField(
        length=8,
        max_length=8,
        prefix="id_",
        primary_key=True,
    )
    id_consultor = models.IntegerField()
    id_administrador = models.IntegerField()
    id_cliente = models.IntegerField()
    hora = models.IntegerField()
    txt_consultor = models.TextField()
    acredita_admin = models.BooleanField()
    txt_admin = models.TextField()
    acredita_cliente = models.BooleanField()
    txt_cliente = models.TextField()
