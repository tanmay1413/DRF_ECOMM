
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView # type: ignore
from rest_framework.permissions import IsAuthenticated

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('product.urls')),
    path('api/', include('account.urls')),
    path("auth/", include('rest_framework.urls', namespace='rest_framework')),  
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name='schema',permission_classes=[IsAuthenticated]), name='swagger-ui'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)