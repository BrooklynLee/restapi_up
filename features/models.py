from django.db import models
from core.models import CoreModel


class Feature(CoreModel):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=140, primary_key=True)
    address = models.CharField(max_length=140)
    price = models.IntegerField(help_text="USD per night")
    beds = models.IntegerField(default=1)
    lat = models.DecimalField(max_digits=10, decimal_places=6)
    lng = models.DecimalField(max_digits=10, decimal_places=6)
    bedrooms = models.IntegerField(default=1)
    bathrooms = models.IntegerField(default=1)
    check_in = models.TimeField(default="00:00:00")
    check_out = models.TimeField(default="00:00:00")
    instant_book = models.BooleanField(default=False)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="features"
    )

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
