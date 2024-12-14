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
  
  def __str__(self):
    return self.name
