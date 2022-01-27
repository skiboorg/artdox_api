from decimal import Decimal

from celery import shared_task
from django.utils.timezone import now
from datetime import timedelta
from .models import *


@shared_task
def checkOrderItems():
    items = OrderItem.objects.all()
    for item in items:
        print(now().date())
        if now().date() == item.pay_date:
            item.total_profit += Decimal(0.025) * Decimal(item.price)
            item.your_profit += Decimal(0.025) * Decimal(item.price)
            item.order.user.pay_summ += Decimal(0.025) * Decimal(item.price)
            item.pay_date = now() + timedelta(days=30)
            item.save()
            item.order.user.save()
    print('checkLessons done')