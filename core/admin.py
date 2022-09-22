from django.contrib import admin
from django.db import models

from core.models import Marca, Categoria, Carro

admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Carro)