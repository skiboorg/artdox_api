from django.db import models
from pytils.translit import slugify
from PIL import Image
from io import BytesIO
from django.core.files import File
from django.utils.safestring import mark_safe

def makeThumb(image):
    fill_color = '#fff'
    base_image = Image.open(image)
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
    return blob


class Collection(models.Model):
    order = models.IntegerField('Порядок', default=100)
    name = models.CharField('Название', max_length=100, blank=False, null=True)
    name_slug = models.CharField('Название', max_length=100, blank=True, null=True, editable=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['order']
        verbose_name = "Коллекция"
        verbose_name_plural = "Коллекции"

class ItemStatus(models.Model):
    name = models.CharField('Статус', max_length=100, blank=False, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"

class Item(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.SET_NULL, null=True, blank=True, related_name='items')
    status = models.ForeignKey(ItemStatus, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField('Название', max_length=100, blank=False, null=True)
    name_slug = models.CharField('Название', max_length=100, blank=True, null=True, editable=False)
    article = models.CharField('Артикул', max_length=20, blank=False, null=True)
    size = models.CharField('Размеры', max_length=20, blank=False, null=True)
    material = models.CharField('Материал', max_length=20, blank=False, null=True)
    description = models.TextField('Описание', blank=True, null=True)
    price = models.IntegerField('Цена', default=0)
    total = models.IntegerField('Тираж', default=0)
    left = models.IntegerField('Остаток', default=0)
    image = models.ImageField('Большое изображение', upload_to='item/full', blank=True, null=True)
    image_thumb = models.ImageField('Маленькое изображение', upload_to='item/thumb', blank=True, null=True)
    image_alt = models.ImageField('Большое изображение', upload_to='item/full', blank=True, null=True)
    image_alt_thumb = models.ImageField('Маленькое изображение', upload_to='item/thumb', blank=True, null=True)
    is_sell = models.BooleanField('Продано?',default=False)
    is_nft = models.BooleanField('NFT',default=False)
    is_ordered = models.BooleanField('Заказана?', default=False)
    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        # self.image_thumb.save(f'{self.name_slug}.jpg',
        #                 File(makeThumb(self.image)), save=False)
        # self.image_alt_thumb.save(f'{self.name_slug}_alt.jpg',
        #                      File(makeThumb(self.image_alt)), save=False)

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def image_tag(self):
        # used in the admin site model as a "thumbnail"
        if self.image:
            return mark_safe(f'<img src="{self.image_thumb.url}" width="235" height="160" />')
        else:
            return mark_safe('<span>НЕТ МИНИАТЮРЫ</span>')

    image_tag.short_description = 'Картинка'