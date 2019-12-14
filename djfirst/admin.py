from django.contrib import admin
from .models import Cart, Item

# Register your models here.
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['cart_item_name', 'cart_item_count']

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['item','item_desc','item_display','item_weight']