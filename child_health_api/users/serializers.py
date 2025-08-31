from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Caregiver

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class CaregiverSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Caregiver
        fields = ['id', 'user', 'phone_number']
