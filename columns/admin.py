from django.contrib import admin
from . import models


@admin.register(models.Column)
class ColumnAdmin(admin.ModelAdmin):
    pass
