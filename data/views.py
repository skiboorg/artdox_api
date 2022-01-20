from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import *
from .serializers import *


class GetBanners(generics.ListAPIView):
    serializer_class = BannerSerializer
    queryset = Banner.objects.all()

class CForm(APIView):
    def post(self,request):

        form = ContactForm.objects.create(
            subject=request.data['subject'],
            email=request.data['email'],
            text=request.data['text'],
        )
        if request.FILES.getlist('file'):
            form.file = request.FILES.getlist('file')[0]
            form.save()
        return Response(status=200)


class RForm(APIView):
    def post(self,request):

        form = ReturnForm.objects.create(
            item_id=request.data['id'],
            text=request.data['text'],
        )
        return Response({'id':form.id},status=200)


class SForm(APIView):
    def post(self,request):
        form = StoreForm.objects.create(
            item_id=request.data['id'],
            text=request.data['text'],
        )
        return Response({'id': form.id}, status=200)


