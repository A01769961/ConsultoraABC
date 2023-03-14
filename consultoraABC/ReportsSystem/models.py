from django.db import models

# Create your models here.
class usuario(models.Model):
    name = models.CharField(max_length=40)
    PlastName = models.CharField(max_length=40)
    MLastName = models.CharField(max_length=40)
    mail = models.CharField(max_length=20)
    