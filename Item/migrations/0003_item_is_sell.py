# Generated by Django 3.2.7 on 2021-09-29 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Item', '0002_auto_20210928_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_sell',
            field=models.BooleanField(default=False, verbose_name='Продано?'),
        ),
    ]
