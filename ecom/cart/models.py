from django.db import models
from account.models import CustomUser 
from product.models import Product
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(CustomUser , on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    total_price = models.FloatField(default=0)


class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser , on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)



@receiver(post_save, sender=CartItems)
def correct_items(sender, **kwargs):
    cart_items = kwargs['instance']
    
    try:
        # Fetch the product price
        product = Product.objects.get(id=cart_items.product.id)
        p = cart_items.quantity * product.price
        CartItems.objects.filter(id=cart_items.id).update(price=p)
    
    except Product.DoesNotExist:
        print(f"Product with id {cart_items.product.id} does not exist.")
