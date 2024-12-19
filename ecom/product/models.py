from django.db import models
from mptt.models import MPTTModel, TreeForeignKey # type: ignore

# Brand model here 
class Brand(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  
  def __str__(self):
    return self.name
  

# Category model here
class Category(MPTTModel):
  name = models.CharField(max_length=100)
  parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
  description = models.TextField()
  
  class MPTTMeta:
        order_insertion_by = ['name']
        
  def __str__(self):
      return self.name
  
  


# Product model here 
class Product(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  price = models.IntegerField()
  brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
  category = TreeForeignKey('Category', on_delete=models.CASCADE)
  image = models.ImageField(upload_to="product_image/", null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.name
  
  
  
# Product Detail models here
class ProductDetail(models.Model):
  product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="Details")
  color = models.CharField(max_length=100)
  size = models.CharField(max_length=100)
  stock = models.IntegerField()
  images = models.ManyToManyField("ProductImage", related_name="product_details")
  reviews = models.TextField(null=True, blank=True)
  rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
  weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
  
  def __str__(self):
        return f"Details for {self.product.name}"
  

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='additional_images')
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"Image for {self.product.name}"
