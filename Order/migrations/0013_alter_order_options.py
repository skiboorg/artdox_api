# Generated by Django 3.2.7 on 2022-02-01 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0012_alter_order_is_in_localstore'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
    ]