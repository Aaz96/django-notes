#django imports
from rest_framework import serializers

#app level imports
from djfirst.models import Cart

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model =Cart
        fields = '__all__'
        field = ['cart_item_name', 'cart_item_count']