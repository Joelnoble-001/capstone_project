from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Caregiver


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

class CaregiverSerializer(serializers.ModelSerializer):
    user = UserSerializer()   # nested

    class Meta:
        model = Caregiver
        fields = ['id', 'user', 'phone_number']

    def create(self, validated_data):
        # Extract user data
        user_data = validated_data.pop('user')
        # Create User
        user = User.objects.create_user(
            username=user_data['username'],
            email=user_data['email'],
            password=user_data['password']
        )
        # Create Caregiver linked to User
        caregiver = Caregiver.objects.create(user=user, **validated_data)
        return caregiver
