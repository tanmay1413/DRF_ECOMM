from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from drf_spectacular.utils import extend_schema # type: ignore

from .models import Brand, Product, Category
from .serializers import BrandSerializer, ProductSerializer, CategorySerializer

# Create your views here.
class BrandViewSet(viewsets.ViewSet):
  queryset = Brand.objects.all()
  serializer_class = BrandSerializer
  
  @extend_schema(request= BrandSerializer)
  def list(self, request):
    serializer = BrandSerializer(self.queryset, many=True)
    print(serializer)
    return Response(serializer.data )
  
  
  def create(self, request):
    data = request.data
    serializer = BrandSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status= status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  
  

class CategoryViewSet(viewsets.ViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  @extend_schema(request = CategorySerializer)
  def list(self, request):
    serializer = CategorySerializer(self.queryset, many=True)
    print(serializer)
    return Response(serializer.data )



class ProductViewSet(viewsets.ViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    @action(
        detail=False,
        methods=["GET"],
        url_path=r"by-category/(?P<category>[^\./]+)/all",  # Match categories with spaces or special characters
        name="list_products_by_category",
    )
    def list_products_by_category(self, request, category=None):
        # Filter products by category name
        products = Product.objects.filter(category__name__iexact=category)  # Case-insensitive match
        serializer = ProductSerializer(products, many=True) 
        return Response(serializer.data)  
      
    @extend_schema(request = ProductSerializer) 
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)