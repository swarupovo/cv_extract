import random

from django_seed import Seed
from faker import Faker
from api.models import Profile


seeder = Seed.seeder()

seeder.add_entity(Profile, 5, {
    'name': lambda x: Faker.name(),
    'email': lambda x: Faker.email(),
})
# seeder.add_entity(Player, 10)

inserted_pks = seeder.execute()