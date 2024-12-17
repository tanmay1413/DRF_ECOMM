from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from drf_spectacular.utils import extend_schema # type: ignore

from .models import Brand, Product, Category
from .serializers import BrandSerializer, ProductSerializer, CategorySerializer



# Create your views here.
@extend_schema(
    tags=["Brand"],  
    request=BrandSerializer, 
    responses=BrandSerializer,  
    description="CRUD operations for Brand"
)
class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer




@extend_schema(
    tags=["Category"],  # Groups this viewset in the API docs
    request=CategorySerializer,  # Default request schema for all actions
    responses=CategorySerializer,  # Default response schema for all actions
    description="CRUD operations for Category"
)
class CategoryViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions for Category.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



# @extend_schema(
#     tags=["Product"],  
#     request=ProductSerializer, 
#     responses=ProductSerializer,  
#     description="CRUD operations for Product"
# )
# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
    
#     @action(
#         detail=False,
#         methods=["GET"],
#         url_path=r"by-category/(?P<category>[^\./]+)/all",  # Match categories with spaces or special characters
#         name="list_products_by_category",
#     )
#     def list_products_by_category(self, request, category=None):
#         # Filter products by category name
#         products = Product.objects.filter(category__name__iexact=category)  # Case-insensitive match
#         serializer = ProductSerializer(products, many=True) 
#         return Response(serializer.data)  
    
@extend_schema(
    tags=["Product"],  
    request=ProductSerializer, 
    responses=ProductSerializer(many=True),  
    description="Filter products by name, category, and/or brand   [use /?name=name, ?category=category, ?brand=brand]",
    
 
)
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(
        detail=False,
        methods=["GET"],
        url_path="filter",
        name="filter_products",
    )
    def filter_products(self, request):
        """
        Filter products by name, category, and/or brand.
        """
        products = Product.objects.all()

        # Filter by category
        category = request.query_params.get("category")
        if category:
            products = products.filter(category__name__iexact=category)

        # Filter by brand
        brand = request.query_params.get("brand")
        if brand:
            products = products.filter(brand__name__iexact=brand)

        # Filter by product name
        name = request.query_params.get("name")
        if name:
            products = products.filter(name__icontains=name)

        # Serialize and return the filtered products
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    