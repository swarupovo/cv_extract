from django.test import TestCase
from faker import Faker
from api.models import Profile


class ProfileTestCase(TestCase):
    def setUp(self):
        self.faker = Faker()
        for _ in range(10):
            Profile.objects.create(name=self.faker.first_name(), email=self.faker.email())

    def test_profile_has_data(self):
        swt = Profile.objects.get(name="Melissa Rios")
        print(swt.name)

        self.assertEqual(swt.full_name, 'Melissa Rios')




