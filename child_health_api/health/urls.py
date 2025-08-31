from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChildViewSet, HealthRecordViewSet, VaccinationViewSet


router = DefaultRouter()
router.register(r'children', ChildViewSet, basename='child')
router.register(r'health-records', HealthRecordViewSet, basename='healthrecord')
router.register(r'vaccinations', VaccinationViewSet, basename='vaccination')

urlpatterns = [
    path('', include(router.urls)),
]
