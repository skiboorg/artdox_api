from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import *
#from .serializers import *

from Cart.views import getCart


class CreateOrder(APIView):
    def post(self,request):
        cart = getCart(request)
        new_order = Order.objects.create(user=request.user)
        price = 0
        for item in cart.items.all():
            new_order.items.add(item)
            price += item.price
            cart.items.remove(item)
        new_order.price = price
        new_order.save()
        cart.save()
        return Response(status=200)




