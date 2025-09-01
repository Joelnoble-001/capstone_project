from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .models import Child, Caregiver, HealthRecord, Vaccination
from .serializers import ChildSerializer, HealthRecordSerializer, VaccinationSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class ChildViewSet(viewsets.ModelViewSet): 
    serializer_class = ChildSerializer 
    permission_classes = [permissions.IsAuthenticated] 
    
    @action(detail=True, methods=['get']) 
    def full_details(self, request, pk=None): 
        child = self.get_object()
        serializer = ChildDetailSerializer(child) 
        return Response(serializer.data) 
        
    def get_queryset(self): 
        # Show only the children of the logged-in caregiver 
        return Child.objects.filter(caregiver=self.request.user) 
    
    def perform_create(self, serializer): # Attach caregiver automatically 
        serializer.save(caregiver=self.request.user)
        

class HealthRecordViewSet(viewsets.ModelViewSet):
    queryset = HealthRecord.objects.all()
    serializer_class = HealthRecordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only allow records for the logged-in user's children
        return HealthRecord.objects.filter(child__caregiver=self.request.user)


class VaccinationViewSet(viewsets.ModelViewSet):
    queryset = Vaccination.objects.all()
    serializer_class = VaccinationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only allow vaccinations for the logged-in user's children
        return Vaccination.objects.filter(child__caregiver=self.request.user)
