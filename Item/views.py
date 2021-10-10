from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import *
from .serializers import *

class GetItems(generics.ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        if self.request.query_params.get('type')=='all':
            return Item.objects.all()
        if self.request.query_params.get('type')=='index':
            return Item.objects.all()[:10]

class GetItem(generics.RetrieveAPIView):
    serializer_class = ItemSerializer

    def get_object(self):
       return Item.objects.get(name_slug=self.request.query_params.get('slug'))


class GetCollections(generics.ListAPIView):
    serializer_class = CollectionSerializer
    queryset = Collection.objects.all()