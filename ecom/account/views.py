from rest_framework import viewsets,  views 
from rest_framework.response import Response
from .models import CustomUser
from .serializer import CustomUserSerializer , UserLoginSerializer
from django.contrib.auth import authenticate, login , logout
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework import status, viewsets
from rest_framework_simplejwt.tokens import RefreshToken # type: ignore
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

    # Allow anyone to register a new user
    permission_classes_by_action = {
        'create': [AllowAny],
        'default': [IsAuthenticated],
    }

    def get_permissions(self):
        return [permission() for permission in self.permission_classes_by_action.get(self.action, self.permission_classes_by_action['default'])]

    def create(self, request, *args, **kwargs):
        # Create a new user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()  

        # Generate tokens for the newly registered user
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        # Return the serialized user data with the tokens
        return Response({
            "user": serializer.data,
            "tokens": {
                "access": access_token,
                "refresh": refresh_token,
            }
        }, status=status.HTTP_201_CREATED)
    
    
 
 
@extend_schema(
        tags=["Login"],  
        request=UserLoginSerializer,
        responses={200: "Login Successful", 401: "Unauthorized"},
    ) 
class UserLogin(views.APIView):
    permission_classes = [IsAuthenticated] 
  
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
  
        phone_number = serializer.validated_data.get('phone_number')
        password = serializer.validated_data.get('password')
        user = None
        
        if phone_number:
            user = authenticate(request, username=phone_number, password=password)

        if user:
            login(request, user)
            return Response({'Message': "Login Successful"}, status=200)

        return Response({'error': 'Invalid credentials'}, status=401)



@extend_schema(
        tags=["Logout"],  
        request=UserLoginSerializer,
        responses={200: "Logout Successful", 401: "Unauthorized"},
    )
class UserLogout(views.APIView):
    # permission_classes = [IsAuthenticated] 
   
    def get(self, request):
        logout(request)
        return Response({"massage": "Logout Successful"})