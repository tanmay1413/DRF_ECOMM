from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from drf_spectacular.utils import extend_schema # type: ignore

from .models import Brand, Product, Category , ProductImage, ProductDetail
from .serializers import BrandSerializer, ProductSerializer, CategorySerializer , ProductDetailSerializer , ProductImageSerializer



# Create your views here.
@extend_schema(
    tags=["Brand"],  
    request=BrandSerializer, 
    responses=BrandSerializer,  
    description="CRUD operations for Brand"
)
class BrandViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer




@extend_schema(
    tags=["Category"],  
    request=CategorySerializer,  
    responses=CategorySerializer, 
    description="CRUD operations for Category"
)
class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


    
@extend_schema(
    tags=["Product"],  
    request=ProductSerializer, 
    responses=ProductSerializer(many=True),  
    description="Filter products by name, category, and/or brand   [use /?name=name, ?category=category, ?brand=brand]",
    
)
class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
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
    
@extend_schema(
    tags=["Product Detail"],  
    request=ProductDetailSerializer, 
    responses=ProductDetailSerializer,  
)
class ProductDetailView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ProductDetail.objects.all()
    serializer_class = ProductDetailSerializer
    
@extend_schema(
    tags=["Product Image"],  
    request=ProductImageSerializer, 
    responses=ProductImageSerializer,  
) 
class ProductImagesView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    