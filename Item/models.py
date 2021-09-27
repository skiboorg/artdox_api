from django.db import models
from pytils.translit import slugify
from PIL import Image
from io import BytesIO
from django.core.files import File
from django.utils.safestring import mark_safe


class Item(models.Model):
    name = models.CharField('Название', max_length=100, blank=False, null=True)
    name_slug = models.CharField('Название', max_length=100, blank=True, null=True, editable=False)
    article = models.CharField('Артикул', max_length=20, blank=False, null=True)
    size = models.CharField('Размеры', max_length=20, blank=False, null=True)
    material = models.CharField('Материал', max_length=20, blank=False, null=True)
    description = models.TextField('Описание', blank=True, null=True)
    price = models.IntegerField('Цена', default=0)
    image = models.ImageField('Большое изображение', upload_to='item/full', blank=True, null=True)
    image_thumb = models.ImageField('Маленькое изображение', upload_to='item/thumb', blank=True, null=True)

    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        fill_color = '#fff'
        base_image = Image.open(self.image)
        blob = BytesIO()
        if base_image.mode in ('RGBA', 'LA'):
            background = Image.new(base_image.mode[:-1], base_image.size, fill_color)
            background.paste(base_image, base_image.split()[-1])
            base_image = background

        width, height = base_image.size
        transparent = Image.new('RGB', (width, height), (0, 0, 0, 0))
        transparent.paste(base_image, (0, 0))
        transparent.thumbnail((235, 160), Image.ANTIALIAS)
        transparent.save(blob, 'png', quality=100, optimize=True)
        self.image_thumb.save(f'{self.name_slug}.jpg',
                        File(blob), save=False)

        super().save(*args, **kwargs)

    def image_tag(self):
        # used in the admin site model as a "thumbnail"
        if self.image:
            return mark_safe(f'<img src="{self.image_thumb.url}" width="235" height="160" />')
        else:
            return mark_safe('<span>НЕТ МИНИАТЮРЫ</span>')

    image_tag.short_description = 'Картинка'