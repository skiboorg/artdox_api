import json
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .services import create_random_string
from .serializers import *
from .models import *
from rest_framework import generics

from django.core.mail import send_mail
from django.template.loader import render_to_string

import settings

class UserUpdate(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user

        print(json.loads(request.data['userData']))

        password = None
        try:
            password = json.loads(request.data['password'])
        except:
            pass

        selected_avatar = None
        try:
            selected_avatar = json.loads(request.data['selected_avatar'])
        except:
            pass
        print(selected_avatar)
        serializer = UserSerializer(user, data=json.loads(request.data['userData']))
        if password:
            user.set_password(password)
            user.save()
        if serializer.is_valid():
            serializer.save()
            for f in request.FILES.getlist('avatar'):
                user.avatar = f
                user.save(force_update=True)
            return Response(status=200)
        else:
            print(serializer.errors)
            return Response(status=400)


class GetUser(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class UserRecoverPassword(APIView):
    def post(self,request):
        user = None
        try:
            user = User.objects.get(email=request.data['email'])
        except:
            user = None
        if user:
            password = create_random_string(digits=True, num=8)
            user.set_password(password)
            user.save()
            return Response({'result': True, 'email': user.email}, status=200)
        else:
            return Response({'result': False}, status=200)

class WithdrawalRequestView(APIView):
    def post(self, request):
        payment_type = request.data.get('payment_type')
        if payment_type != 0:
            item = WithdrawalRequest.objects.create(user=request.user,
                                                    payment_type_id=payment_type,
                                                    message=request.data.get('message'),
                                                    )
        else:
            item = WithdrawalRequest.objects.create(user=request.user,
                                                    message=request.data.get('message'),
                                                    )
        msg_html = render_to_string('withdrawal.html', {
            'id': item.id,
            'user': request.user,
            'amount': request.user.pay_summ
        })

        send_mail(f'Запрос №{item.id} на вывод', None, settings.SMTP_FROM, [settings.ADMIN_EMAIL,request.user.email],
                  fail_silently=False, html_message=msg_html)
        return Response({'id':item.id}, status=200)

class PaymentSystems(generics.ListAPIView):
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer

class CForm(APIView):
    def post(self,request):
        if request.data.get('user_id'):
            ContactForm.objects.create(
                user_id=request.data['user_id'],
                subject=request.data['subject'],
                email=request.data['email'],
                text=request.data['text'],
            )
        else:

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

        msg_html = render_to_string('return_client.html', {
            'id': form.id,
            'user': request.user,
            'item':form.item
        })

        send_mail(f'Запрос №{form.id} на возврат картины', None, settings.SMTP_FROM, [settings.ADMIN_EMAIL,request.user.email],
                  fail_silently=False, html_message=msg_html)
        return Response({'id':form.id},status=200)


class SForm(APIView):
    def post(self,request):
        form = StoreForm.objects.create(
            item_id=request.data['id'],
            text=request.data['text'],
        )
        msg_html = render_to_string('store.html', {
            'id': form.id,
            'user': request.user,
            'item': form.item
        })

        send_mail(f'Запрос №{form.id} на заклад картины', None, settings.SMTP_FROM, [settings.ADMIN_EMAIL,request.user.email],
                  fail_silently=False, html_message=msg_html)
        return Response({'id': form.id}, status=200)