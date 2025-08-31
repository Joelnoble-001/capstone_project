from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .models import Caregiver
from .serializers import CaregiverSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# Create your views here.

class RegisterCaregiverView(generics.CreateAPIView):
    queryset = Caregiver.objects.all()
    serializer_class = CaregiverSerializer

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'user_id': token.user_id})
