# backend/moms_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

urlpatterns = [
    path('', index, name='index'),  # main app point to admin site
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/hr/', include('apps.hr.urls')),
    path('api/analytics/', include('apps.analytics.urls')),
    path('api/automation/', include('apps.automation.urls')),
    path('api/collaboration/', include('apps.collaboration.urls')),
    path('api/compliance/', include('apps.compliance.urls')),
    path('api/crm/', include('apps.crm.urls')),
    path('api/finance/', include('apps.finance.urls')),
    path('api/project/', include('apps.project.urls')),
    path('api/strategy/', include('apps.strategy.urls')),
    path('api/supply_chain/', include('apps.supply_chain.urls')),

    # Add browsable API
    path('api-auth/', include('rest_framework.urls')), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    # Add debug toolbar URLs if installed
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [
            path('__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns