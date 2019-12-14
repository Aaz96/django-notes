from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class Cart(models.Model):
    cart_item_name = models.CharField(max_length = 64, default ='arbitrry item')
    cart_item_count = models.IntegerField(default = 0)

    def __str__(self):
        return str(self.cart_item_name)

class Item(models.Model):
    item = models.ForeignKey('Cart', on_delete= models.PROTECT, related_name= 'cart_item')
    item_desc = models.TextField()
    item_display = models.DateTimeField(default = datetime.now()+timedelta(days = 15))
    item_weight = models.FloatField(default =0)