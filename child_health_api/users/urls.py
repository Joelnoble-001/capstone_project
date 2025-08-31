from django.urls import path
from .views import RegisterCaregiverView, CustomAuthToken

urlpatterns = [
    path('register/', RegisterCaregiverView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
]