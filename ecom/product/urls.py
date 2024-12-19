
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, BrandViewSet, CategoryViewSet, ProductDetailView, ProductImagesView

router = DefaultRouter()
router.register(r'product',ProductViewSet, basename='product')
router.register(r'brand',BrandViewSet, basename='brand')
router.register(r'category',CategoryViewSet, basename='category')
router.register(r'product-detail',ProductDetailView , basename='product-detail-view' )
router.register(r'product-image', ProductImagesView, basename='product-image')


urlpatterns = [
   path('', include(router.urls)),
]
    

