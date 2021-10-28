from django.contrib import admin

# Register your models here.
from .models import Cliente

class ClienteAdmin(admin.ModelAdmin):
	list_display=('nombres', 'apellidos', 'dni', 'celular', 'email')

admin.site.register(Cliente,ClienteAdmin)
