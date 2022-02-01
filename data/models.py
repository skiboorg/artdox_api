from django.db import models


class Banner(models.Model):
    image = models.ImageField('Баннер', upload_to='banner', blank=True, null=True)
    image_mob = models.ImageField('Баннер мобильный', upload_to='banner', blank=True, null=True)

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"


class ContactForm(models.Model):
    subject = models.CharField('Название', max_length=100, blank=True, null=True)
    email = models.CharField('email', max_length=100, blank=True, null=True)
    text = models.TextField('Текст', blank=True, null=True)
    file = models.ImageField('Баннер', upload_to='form', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return f'Форма обратной связи от {self.email} | {self.created_at}'

    class Meta:
        verbose_name = "Форма обратной связи"
        verbose_name_plural = "Формы обратной связи"


class ReturnForm(models.Model):
    item = models.ForeignKey('Order.OrderItem', on_delete=models.CASCADE,blank=True, null=True)
    text = models.TextField('Текст', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return f'№{self.id} | Запрос на возврат от {self.item.order.user.email} | {self.created_at}'

    class Meta:
        verbose_name = "Запрос на возврат"
        verbose_name_plural = "Запросы на возврат"


class StoreForm(models.Model):
    item = models.ForeignKey('Order.OrderItem', on_delete=models.CASCADE,blank=True, null=True)
    text = models.TextField('Текст', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_in_store = models.BooleanField(default=False)
    is_return_store = models.BooleanField(default=False)
    is_done = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.is_in_store:
            self.item.order.user.total_in_store += self.item.amount
            self.item.is_in_store = True
            self.item.order.user.save()
            self.item.save()
        if self.is_return_store:
            self.item.order.user.total_in_store -= self.item.amount
            self.item.is_in_store = False
            self.item.order.user.save()
            self.item.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'№{self.id} | Запрос на заклад от {self.item.order.user.email} | {self.created_at}'

    class Meta:
        verbose_name = "Запрос на заклад"
        verbose_name_plural = "Запросы на заклад"