# backend/apps/analytics/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DashboardViewSet, ReportViewSet

router = DefaultRouter()
router.register(r'dashboards', DashboardViewSet)
router.register(r'reports', ReportViewSet)

urlpatterns = router.urls
"""
[
    path('', include(router.urls)),
]
"""