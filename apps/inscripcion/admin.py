from django.contrib import admin
from .models import Usuario, Horario, dias
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Horario)
admin.site.register(dias)