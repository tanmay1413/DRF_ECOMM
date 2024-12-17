
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet

router = DefaultRouter()
router.register(r'', CustomUserViewSet, basename='account')



urlpatterns = [
  path('', include(router.urls)),
]
    

