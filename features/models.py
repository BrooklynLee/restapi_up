from django.db import models
from core.models import CoreModel


class FeatureType(models.Model):
    type_name = models.CharField(max_length=30)
    # parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)

    # class Meta:
    #     unique_together = ["category_name"]

    def __str__(self):
        return self.type_name


class Tag(models.Model):
    name = models.CharField(max_length=32, verbose_name="태그명")
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "feature_tag"


class Feature(CoreModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=140)
    desc = models.TextField(blank=True)
    # category = models.CharField(max_length=140)
    link = models.CharField(max_length=140, help_text="Confluence Link")
    feature_type = models.ForeignKey(FeatureType, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="features"
    )
    tag = models.ManyToManyField("Tag", null=True)

    def __str__(self):
        return self.name

    def photo_number(self):
        return self.photos.count()

    photo_number.short_description = "Photo Count"

    class Meta:
        ordering = ["-pk"]


class Photo(CoreModel):

    file = models.ImageField()
    feature = models.ForeignKey(
        "features.Feature", related_name="photos", on_delete=models.CASCADE
    )
    caption = models.CharField(max_length=140)

    def __str__(self):
        return self.feature.name
