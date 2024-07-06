from django.db import models

# Create your models here. MODELS SON CLASES QUE AYUDAN A GESTIONAR LA CONEXION CON LA BASE DE DATOS

class Pokemon(models.Model):
    name = models.CharField(max_length=30,null=False)
    type = models.CharField(max_length=30,null=False)
    weight = models.IntegerField(null=False)
    height = models.IntegerField(null=False)
    
    def __str__(self) -> str:
        return self.name