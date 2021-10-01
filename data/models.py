from django.db import models


class Banner(models.Model):
    image = models.ImageField('Баннер', upload_to='banner', blank=True, null=True)
    image_mob = models.ImageField('Баннер мобильный', upload_to='banner', blank=True, null=True)


class ContactForm(models.Model):
    subject = models.CharField('Название', max_length=100, blank=True, null=True)
    text = models.TextField('Текст', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)