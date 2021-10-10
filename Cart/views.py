from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import *
from .serializers import *




class GetCart(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    def get_object(self):
        return Cart.objects.get(user=self.request.user)


class AddToCart(APIView):
    def post(self,request):
        cart = Cart.objects.get(user=self.request.user)
        data = request.data
        item, created = CartItem.objects.get_or_create(defaults={'item_id':data['id'],'cart':cart})
        if created:
            item.amount = data['amount']
        else:
            item.amount += data['amount']
        item.save()

        return Response(status=200)