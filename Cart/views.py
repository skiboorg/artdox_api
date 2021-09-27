from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import *
from .serializers import *

def getCart(request):
    try:
        cart = Cart.objects.get(user=request.user)
    except:
        cart = Cart.objects.create(user=request.user)
    return cart


class GetCart(generics.RetrieveAPIView):
    serializer_class = CartSerializer

    def get_object(self):
        return getCart(self.request)


class AddToCart(APIView):
    def post(self,request):
        cart = getCart(request)
        data = request.data
        cart.items.add(data['id'])
        return Response(status=200)