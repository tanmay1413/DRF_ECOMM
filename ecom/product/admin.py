from django.contrib import admin
from .models import *


admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductDetail)
admin.site.register(ProductImage)