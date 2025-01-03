from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Cart , CartItems
from .serializers import CartSerializer , CartItemsSerializer
from product.models import Product , ProductDetail
from account.models import CustomUser
from drf_spectacular.utils import extend_schema # type: ignore



@extend_schema(
    tags=["Cart"],  
    request=CartSerializer, 
    responses=CartSerializer(many=True),  
    description="Cart",
)
class CartView(APIView):
  permission_classes = [IsAuthenticated]


  def get(self, request):
    user = request.user
    cart = Cart.objects.filter(user=user, ordered=False).first()
    
    if not cart:
      return Response({"message": "No active cart found."}, status=404)
    
    cart_items = CartItems.objects.filter(cart=cart).select_related('user', 'product', 'cart') 
    serializer = CartItemsSerializer(cart_items, many=True)
    return Response(serializer.data)
  
  def post(self , request):
    data = request.data 
    user = request.user
    cart,_ = Cart.objects.get_or_create(user = user, ordered = False)
    product = Product.objects.get(id = data.get('product'))
    price = product.price
    quantity = data.get('quantity')
    
    cart_items = CartItems( cart = cart , user = user , product = product, price = price , quantity = quantity )
    cart_items.save() 
    
    total_price = 0 
    print(cart.id)
    cart_items = CartItems.objects.filter(user = user ,cart = cart.id)
    for items in cart_items:
      total_price += items.price
      cart.total_price = total_price
      cart.save()
    return Response({'Success':'Iteam added to the cart!!'})
    
  
  def patch(self , request):
    data = request.data
    cart_item = CartItems.objects.get(id = data.get('id'))
    quantity = int(data.get('quantity'))
    cart_item.quantity += quantity
    cart_item.save()
    return Response({'Success':'Iteam Updated!!'})
    
  
  def delete(self , request):
    user = request.user
    data = request.data
    
    cart_item = CartItems.objects.get(id = data.get('id'))
    cart_item.delete()

    cart = Cart.objects.filter(user=user, ordered=False).first()    
    if not cart:
      return Response({"message": "No active cart found."}, status=404)
    
    cart_items = CartItems.objects.filter(cart=cart).select_related('user', 'product', 'cart') 
    serializer = CartItemsSerializer(cart_items, many=True)
    return Response(serializer.data)
 