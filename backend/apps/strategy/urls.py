# backend/apps/strategy/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StrategicPlanViewSet, GoalViewSet, ObjectiveViewSet, KeyResultViewSet

router = DefaultRouter()
router.register(r'plans', StrategicPlanViewSet)
router.register(r'goals', GoalViewSet)
router.register(r'objectives', ObjectiveViewSet)
router.register(r'key-results', KeyResultViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
