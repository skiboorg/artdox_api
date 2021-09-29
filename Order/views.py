from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import *
from Cart.models import *
from user.models import *
#from .serializers import *




class CreateOrder(APIView):
    def post(self,request):
        cart = Cart.objects.get(user=self.request.user)
        new_order = Order.objects.create(user=request.user)
        price = 0
        for item in cart.items.all():
            new_order.items.add(item)
            item.is_sell = True
            price += item.price
            cart.items.remove(item)
            item.save()
        new_order.price = price
        new_order.save()
        cart.save()
        Transaction.objects.create(user=self.request.user, amount = price, is_buy = True, type='VISA')
        return Response(status=200)




