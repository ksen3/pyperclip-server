from django.contrib import admin
from .models import *


class DataAdmin(admin.ModelAdmin):
    list_display = ['user', 'ip', 'time']
    ordering = ['-time']


admin.site.register(Data, DataAdmin)
