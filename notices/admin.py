from django.contrib import admin
from . import models


@admin.register(models.Notice)
class NoticeAdmin(admin.ModelAdmin):
    pass
