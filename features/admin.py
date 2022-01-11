from django.contrib import admin
from . import models


@admin.register(models.Feature)
class FeatureAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "photo_number",
    )


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass


@admin.register(models.FeatureType)
class FeatureTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "registered_date",
    )
