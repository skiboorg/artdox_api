from django.db import models



class Banner(models.Model):
    image = models.ImageField('Баннер', upload_to='banner', blank=True, null=True)
