from django.contrib import admin
from .models import Brand, Category, Product, ProductDetail, ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'brand', 'category']
    search_fields = ['name', 'brand__name', 'category__name']
    list_filter = ['brand__name', 'price','category__name']


class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']  
    search_fields = ['name']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']  
    search_fields = ['name']


admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductDetail)
admin.site.register(ProductImage)
