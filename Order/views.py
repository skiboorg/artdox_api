from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import *
from Cart.models import *
from user.models import *
from .serializers import *
import requests
import settings
import json

def init_payment(order):
    headers = {
                  'Content-Type': 'application/json',
                }
    order_items = order.order_items.all()
    order_user = order.user
    items = []

    for order_item in order_items:
        items.append(
            {
                "Name": order_item.item.name,
                "Price": order_item.item.price * 100,
                "Quantity": order_item.amount,
                "Amount": order_item.price * 100,
                "PaymentMethod": "full_payment",
                "PaymentObject": "commodity",
                "Tax": "vat10",
                "Ean13": "0123456789"
            },
        )

    payload = {
        "TerminalKey": settings.TERMINAL_ID,
        "Amount": order.price * 100,
        "OrderId": order.id,
        "Description": f'Оплата заказа №{order.id}',
        "NotificationURL": 'https://artdox.ru/api/order/payment_notify',
        # "DATA": {
        #     "Phone": "+71234567890",
        #     "Email": "a@test.com"
        # },
        "Receipt": {
            "Email": order.user.email,
            "Phone": order.user.phone,
            "EmailCompany": "b@test.ru",
            "Taxation": "osn",
            "Items": items
        }
    }
    print(payload)
    response = requests.post(settings.INIT_PAYMENT_URL, data=json.dumps(payload), headers=headers)
    response_json = response.json()
    if response_json['Success']:
        print(response_json['PaymentURL'])
        return {'success': True, 'payment_url':response_json['PaymentURL']}
    else:
        return {'success': False}

class CreateOrder(APIView):
    def post(self,request):
        cart = Cart.objects.get(user=self.request.user)
        new_order = Order.objects.create(user=request.user,
                                         delivery=request.data.get('delivery'),
                                         address=request.data.get('address'),
                                         )

        for item in cart.items.all():
            OrderItem.objects.create(order=new_order,
                                     item=item.item,
                                     amount=item.amount)

            item.item.left -= item.amount
            item.item.save()
            request.user.total_amount += item.amount
            item.delete()

        cart.price = 0
        cart.save()

        request.user.total_summ += new_order.price
        request.user.save()

        Transaction.objects.create(user=self.request.user,
                                   amount=new_order.price,
                                   is_buy=True,
                                   type='CARD')
        result = init_payment(new_order)
        return Response(result, status=200)


class GetOrders(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

class PaymentNotify(APIView):
    def post(self, request):
        print(request.data)
        data = request.data
        payment_success = data['Success']
        if payment_success:
            order_id = data['OrderId']
            print(order_id)
            order = Order.objects.get(id=order_id)
            order.is_pay = True
            order.save()
        return Response(status=200)
