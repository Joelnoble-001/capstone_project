from rest_framework import serializers
from .models import Child, HealthRecord, Vaccination

class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = ['id', 'first_name', 'last_name', 'dob', 'gender']
        read_only_fields = ['caregiver']

class HealthRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthRecord
        fields = '__all__'

class VaccinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccination
        fields = '__all__'

class ChildDetailSerializer(serializers.ModelSerializer):
    health_records = HealthRecordSerializer(many=True, read_only=True)
    vaccinations = VaccinationSerializer(many=True, read_only=True)

    class Meta:
        model = Child
        fields = ['id', 'first_name', 'last_name', 'dob', 'gender', 'health_records', 'vaccinations']
