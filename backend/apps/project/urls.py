# backend/apps/project/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, TaskViewSet, TimeEntryViewSet, MilestoneViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'time-entries', TimeEntryViewSet)
router.register(r'milestones', MilestoneViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
