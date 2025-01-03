from django.contrib import admin
from .models import Cart, CartItems

class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'ordered', 'total_price']
    search_fields = ['user__phone_number', 'user__email']  
    list_filter = ['ordered']

class CartItemsAdmin(admin.ModelAdmin):
    list_display = ['user','cart','product','price','quantity']
    search_fields = ['product__name','user__phone_number', 'user__email']  
    list_filter = ['quantity','product__category__name']

# Register your models here.
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItems, CartItemsAdmin)
