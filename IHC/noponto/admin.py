from django.contrib import admin

from django.contrib import admin
from .models import Linha, Rota, Onibus, Horario

admin.site.register(Linha)
admin.site.register(Rota)
admin.site.register(Onibus)
admin.site.register(Horario)
