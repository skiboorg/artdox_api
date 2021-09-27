from django.db import models

class Cart(models.Model):
    user = models.ForeignKey('user.User',on_delete=models.CASCADE, null=True, blank=True,related_name='cart')
    items = models.ManyToManyField('Item.Item', blank=True)
    price = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.price = 0
        for item in self.items.all():
            self.price += item.price

        super().save(*args, **kwargs)

