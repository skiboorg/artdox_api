# Generated by Django 3.2.7 on 2021-09-26 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Название')),
                ('name_slug', models.CharField(blank=True, editable=False, max_length=100, null=True, verbose_name='Название')),
                ('article', models.CharField(max_length=20, null=True, verbose_name='Артикул')),
                ('size', models.CharField(max_length=20, null=True, verbose_name='Размеры')),
                ('material', models.CharField(max_length=20, null=True, verbose_name='Материал')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('image', models.ImageField(blank=True, null=True, upload_to='item/full', verbose_name='Большое изображение')),
                ('image_thumb', models.ImageField(blank=True, null=True, upload_to='item/thumb', verbose_name='Маленькое изображение')),
            ],
        ),
    ]
