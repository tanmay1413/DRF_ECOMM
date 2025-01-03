from rest_framework.serializers import ModelSerializer
from .models import Cart , CartItems
from product.serializers import ProductSerializer, ProductDetailSerializer
from account.serializer import CustomUserSerializer


class CartSerializer(ModelSerializer):
  class Meta:
    model = Cart
    fields = ['id', 'user', 'total_price', 'ordered'] 

class CartItemsSerializer(ModelSerializer):
  user = CustomUserSerializer()
  product = ProductSerializer()

  cart = CartSerializer() 
  class Meta:
    model = CartItems
    fields = ['id', 'cart', 'user', 'product', 'quantity', 'price']