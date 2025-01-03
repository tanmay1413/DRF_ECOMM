

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, UserLogin, UserLogout
from rest_framework_simplejwt.views import ( # type: ignore
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
# Router for ViewSet-based endpoints
router = DefaultRouter()
router.register(r'accounts', CustomUserViewSet, basename='account')  


urlpatterns = [
    path('', include(router.urls)), 
    path('login/', UserLogin.as_view(), name='user-login'), 
    path('logout/', UserLogout.as_view(), name='user-logout'),   
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
