import random
from datetime import datetime
from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User
from features.models import Feature, Photo


class Command(BaseCommand):

    help = "It seeds the DB with tons of stuff"

    def handle(self, *args, **options):
        user_seeder = Seed.seeder()
        user_seeder.add_entity(User, 20, {"is_staff": False, "is_superuser": False})
        user_seeder.execute()

        users = User.objects.all()
        feature_seeder = Seed.seeder()
        feature_seeder.add_entity(
            Feature,
            150,
            {
                "user": lambda x: random.choice(users),
                "name": lambda x: feature_seeder.faker.street_address(),
                "price": lambda x: random.randint(0, 300),
                "beds": lambda x: random.randint(0, 5),
                "bedrooms": lambda x: random.randint(0, 3),
                "bathrooms": lambda x: random.randint(0, 5),
                "instant_book": lambda x: random.choice([True, False]),
                "check_in": lambda x: datetime.now(),
                "check_out": lambda x: datetime.now(),
            },
        )
        feature_seeder.execute()

        feature = Feature.objects.all()
        for room in feature:
            for i in range(random.randint(5, 10)):
                Photo.objects.create(
                    caption=feature_seeder.faker.sentence(),
                    feature=feature,
                    file=f"room_photos/{random.randint(1, 31)}.webp",
                )
        self.stdout.write(self.style.SUCCESS(f"Everything seeded"))
