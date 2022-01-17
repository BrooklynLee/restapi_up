from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    # avatar = models.ImageField(upload_to="avatars", blank=True)
    superhost = models.BooleanField(default=False)
    favs = models.ManyToManyField("features.Feature", related_name="favs")

    def feature_count(self):
        return self.features.count()

    feature_count.short_description = "Feature Count"
