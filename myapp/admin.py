from django.contrib import admin
from .models import Proyecto,User

# Register your models here.

class ProyectoAdmin(admin.ModelAdmin):
    readonly_fields = ['created',]

admin.site.register(Proyecto,ProyectoAdmin)