from django.db import models
from django import forms


class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    comienzo_pro = models.DateTimeField()
    final_pro= models.DateTimeField()
    descripcion= models.CharField(max_length=300)
    def __str__(self):  
        return self.nombre
        
class Tarea(models.Model):
    nombre= models.CharField(max_length=100)
    comienzo= models.DateTimeField('Fecha de inicio')
    final= models.DateTimeField('Fecha final')
    proyecto= models.ForeignKey(Proyecto)
    def __str__(self):  
        return self.nombre

# Create your models here.
