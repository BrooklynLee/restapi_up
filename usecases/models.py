from django.db import models
from core.models import CoreModel


class Usecase(CoreModel):
    id = models.AutoField(primary_key=True)
    feature_id = models.ForeignKey(
        "features.Feature",
        related_name="usecases",
        on_delete=models.CASCADE,
        db_column="feature_id",
    )
    name = models.CharField(max_length=140)
    url_link = models.CharField(null=True, max_length=140)
    desc = models.TextField(blank=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
