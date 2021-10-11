from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import *
from Cart.models import *
from user.models import *
from .serializers import *




class CreateOrder(APIView):
    def post(self,request):
        cart = Cart.objects.get(user=self.request.user)
        new_order = Order.objects.create(user=request.user)
        for item in cart.items.all():
            OrderItem.objects.create(order=new_order,item=item.item,amount=item.amount)
            item.delete()
        cart.price = 0
        cart.save()
        Transaction.objects.create(user=self.request.user, amount = new_order.price, is_buy = True, type='VISA')
        return Response(status=200)


class GetOrders(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

