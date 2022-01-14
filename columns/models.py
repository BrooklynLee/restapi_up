from django.db import models
from core.models import CoreModel

# Create your models here.


class Column(CoreModel):
    id = models.AutoField(primary_key=True)
    feature_id = models.ForeignKey(
        "features.Feature",
        related_name="columns",
        on_delete=models.CASCADE,
        db_column="feature_id",
    )
    columns_name = models.CharField(max_length=140)
    columns_name_kr = models.CharField(max_length=140)
    columns_type = models.CharField(max_length=140)
    columns_desc = models.TextField(blank=True)
    standard_y = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.columns_name
