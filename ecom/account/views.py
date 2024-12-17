from rest_framework import viewsets, permissions
from .models import CustomUser
from .serializer import CustomUserSerializer

from drf_spectacular.utils import extend_schema # type: ignore


@extend_schema(
    tags=["Account"],  
    request=CustomUserSerializer, 
    responses=CustomUserSerializer(many=True),  
    description="Account",
)
class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # permission_classes = [permissions.AllowAny]  # Update for better permissions
