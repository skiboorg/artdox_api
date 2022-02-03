from django.db import models


class Banner(models.Model):
    image = models.ImageField('Баннер', upload_to='banner', blank=True, null=True)
    image_mob = models.ImageField('Баннер мобильный', upload_to='banner', blank=True, null=True)
    title = models.TextField('Заголовок', blank=True, null=True)
    text = models.TextField('Текст', blank=True, null=True)
    button_text = models.CharField('Текст на кнопке',max_length=10, blank=True, null=True)
    button_url = models.CharField('Внутренний URL (/gallery)',max_length=10, blank=True, null=True)

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"



