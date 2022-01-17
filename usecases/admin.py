from django.contrib import admin
from . import models


@admin.register(models.Usecase)
class UsecaseAdmin(admin.ModelAdmin):
    pass
