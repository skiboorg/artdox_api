from django.db import models

class Order(models.Model):
    user = models.ForeignKey('user.User',on_delete=models.CASCADE, null=True, blank=True,related_name='orders')
    items = models.ManyToManyField('Item.Item', blank=True)
    price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


