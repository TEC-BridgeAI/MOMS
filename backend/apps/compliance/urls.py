# backend/apps/compliance/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PolicyViewSet, RegulationViewSet, ComplianceTaskViewSet, AuditViewSet

router = DefaultRouter()
router.register(r'policies', PolicyViewSet)
router.register(r'regulations', RegulationViewSet)
router.register(r'tasks', ComplianceTaskViewSet)
router.register(r'audits', AuditViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
