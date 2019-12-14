from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from djfirst.models import Cart
from djfirst.serializers import CartSerializer

# Create your views here.
class CartView(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    @action(methods =['get'], detail=False, url_path ='good_customers')
    def good_customers(self, request):
        good_customers = Cart.objects.filter(cart_item_quanityt__gte =2)
        serializer = CartSerializer(data = good_customers)

        if serializer.is_valid() is False:
            return Response('Hello')
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

