# backend/apps/automation/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkflowViewSet, TaskViewSet, ScheduleViewSet

router = DefaultRouter()
router.register(r'workflows', WorkflowViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'schedules', ScheduleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
