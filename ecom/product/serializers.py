from rest_framework.serializers import ModelSerializer
from .models import Brand , Category, Product, ProductDetail, ProductImage

class BrandSerializer(ModelSerializer):
  class Meta:
    model = Brand
    fields = '__all__'


class CategorySerializer(ModelSerializer):
  class Meta:
    model = Category
    fields = '__all__'


class ProductSerializer(ModelSerializer):
  class Meta:
    model = Product
    fields = '__all__'

class ProductDetailSerializer(ModelSerializer):
  
  class Meta:
    model = ProductDetail
    fields = '__all__'
    
    
class ProductImageSerializer(ModelSerializer):
  class Meta:
    model = ProductImage
    fields = '__all__'