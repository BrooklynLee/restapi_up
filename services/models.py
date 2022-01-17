from django.db import models
from core.models import CoreModel


class Service(CoreModel):
    # id = models.AutoField(primary_key=True)
    # feature_id = models.ForeignKey(
    #     "features.Feature",
    #     related_name="services",
    #     on_delete=models.CASCADE,
    #     db_column="feature_id",
    # )
    serviceid = models.IntegerField(primary_key=True)
    servicename = models.CharField(max_length=140)

    def __str__(self):
        return str(self.serviceid)
