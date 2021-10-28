from django.db import models

# Create your models here.

class Cliente(models.Model):
    """
    Description: Model Description
    """
    nombres=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=50)
    dni=models.CharField(max_length=8)
    celular=models.CharField(max_length=20, null=True)
    email=models.EmailField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name = ("Cliente")
        verbose_name_plural=("Clientes")

    def __str__(self):
    	return self.nombres
