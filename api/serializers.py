from rest_framework import serializers
from .models import Profile, CvUp


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ['id']


class CvUpSerializer(serializers.Serializer):
    file = serializers.FileField()
