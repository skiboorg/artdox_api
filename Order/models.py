from django.db import models



class Order(models.Model):
    user = models.ForeignKey('user.User',on_delete=models.CASCADE, null=True, blank=True)
    price = models.IntegerField(default=0)
    delivery = models.TextField('Доставка', blank=True, null=True)
    address = models.TextField('Адрес', blank=True, null=True)
    is_pay = models.BooleanField('Оплачен', default=False)
    is_in_localstore = models.BooleanField('С хранением?', default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True, related_name='order_items')
    item = models.ForeignKey('Item.Item', on_delete=models.CASCADE, blank=True, null=True)
    amount = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    is_in_store = models.BooleanField('Заложено? ', default=False)
    is_in_localstore = models.BooleanField('Хранение? ',default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    total_profit = models.DecimalField(decimal_places=2,max_digits=8,default=0)
    your_profit = models.DecimalField(decimal_places=2,max_digits=8,default=0)
    pay_date = models.DateField(blank=True, null=True)


    def save(self, *args, **kwargs):
        self.price = self.item.price * self.amount
        self.order.price += self.price
        self.order.save()
        super().save(*args, **kwargs)
