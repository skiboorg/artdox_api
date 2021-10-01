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
        print(request.data)
        ContactForm.objects.create(
            subject=request.data['subject'],
            text=request.data['text'],
        )
        return Response(status=200)


