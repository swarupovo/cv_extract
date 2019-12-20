from django.db import models

# Create your models here.
from rest_framework.fields import JSONField
from upload_validator import FileTypeValidator


class CvUp(models.Model):
    file = models.FileField(upload_to='CV/data/', default='default.pdf')


class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    skill = models.CharField(max_length=1000)
    mobile_number = models.CharField(max_length=15, blank=False, null=False)

    @property
    def full_name(self):
        return self.name
