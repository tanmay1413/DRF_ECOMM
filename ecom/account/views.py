from rest_framework import viewsets, permissions,  views 
from rest_framework.response import Response
from .models import CustomUser
from .serializer import CustomUserSerializer , UserLoginSerializer
from django.contrib.auth import authenticate, login , logout

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
    permission_classes = [permissions.AllowAny]  



class UserLogin(views.APIView):
    permission_classes = [permissions.AllowAny]  
    @extend_schema(
        request=UserLoginSerializer,
        responses={200: "Login Successful", 401: "Unauthorized"},
    )
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        # email = serializer.validated_data.get('email')
        phone_number = serializer.validated_data.get('phone_number')
        password = serializer.validated_data.get('password')

        # Authenticate user using email or phone number
        user = None
        
        if phone_number:
            user = authenticate(request, username=phone_number, password=password)

        if user:
            login(request, user)
            return Response({'Message': "Login Successful"}, status=200)

        return Response({'error': 'Invalid credentials'}, status=401)


class UserLogout(views.APIView):
    @extend_schema(
        request=UserLoginSerializer,
        responses={200: "Login Successful", 401: "Unauthorized"},
    )
    def get(self, request):
        logout(request)
        return Response({"massage": "Logout Successful"})