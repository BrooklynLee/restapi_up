from django.db import models
from core.models import CoreModel


class FeatureType(CoreModel):
    type_name = models.CharField(max_length=30)

    def __str__(self):
        return self.type_name


class StatusType(CoreModel):
    status_type = models.CharField(max_length=30)

    def __str__(self):
        return self.status_type


class KeyType(CoreModel):
    key_type = models.CharField(max_length=30)

    def __str__(self):
        return self.key_type


class File(CoreModel):
    id = models.AutoField(primary_key=True)
    file = models.FileField()
    feature = models.ForeignKey(
        "features.Feature", related_name="files", on_delete=models.CASCADE
    )
    caption = models.CharField(max_length=140)

    def __str__(self):
        return self.feature.name


class Feature(CoreModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=140)
    desc = models.TextField(blank=True)
    # category = models.CharField(max_length=140)
    link = models.CharField(max_length=140, help_text="Confluence Link")
    feature_type = models.ForeignKey(
        "FeatureType", on_delete=models.DO_NOTHING, null=True
    )
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="features"
    )
    status_type = models.ForeignKey(
        "StatusType", on_delete=models.DO_NOTHING, null=True
    )
    key_type = models.ForeignKey("KeyType", on_delete=models.DO_NOTHING, null=True)
    database_name = models.CharField(max_length=140)
    table_name = models.CharField(max_length=140)
    tag = models.ManyToManyField("tags.Tag", null=True)

    def __str__(self):
        return self.name

    def file_number(self):
        return self.files.count()

    file_number.short_description = "File Count"

    class Meta:
        ordering = ["-pk"]
