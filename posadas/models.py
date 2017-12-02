from django.db import models

# Create your models here.
class Posada(models.Model):
    ubicacion=models.CharField(max_length=250)
    nombre=models.CharField(max_length=50)
    fecha=models.DateField()
    horario=models.TimeField()
    tematica=models.CharField(max_length=250)
    email_contacto=models.EmailField()
    imagen_posada=models.URLField(max_length=200)