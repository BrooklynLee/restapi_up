from django.contrib import admin
from . import models


@admin.register(models.Feature)
class FeatureAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "file_number",
    )


@admin.register(models.File)
class FileAdmin(admin.ModelAdmin):
    pass


@admin.register(models.FeatureType)
class FeatureTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.KeyType)
class KeyTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.StatusType)
class StatusTypeAdmin(admin.ModelAdmin):
    pass
