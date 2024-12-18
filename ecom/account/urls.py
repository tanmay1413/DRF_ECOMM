
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import CustomUserViewSet, UserLogin

# router = DefaultRouter()
# router.register(r'', CustomUserViewSet, basename='account')




# urlpatterns = [
#   path('', include(router.urls)),
#   path('login/', UserLogin.as_view(), name='user-login'),
  
# ]
    

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, UserLogin, UserLogout

# Router for ViewSet-based endpoints
router = DefaultRouter()
router.register(r'accounts', CustomUserViewSet, basename='account')  

# Explicitly map APIView endpoints
urlpatterns = [
    path('', include(router.urls)),  # Handles CustomUserViewSet
    path('login/', UserLogin.as_view(), name='user-login'), 
    path('logout/', UserLogout.as_view(), name='user-logout'),   
]
