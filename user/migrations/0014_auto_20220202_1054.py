# Generated by Django 3.2.7 on 2022-02-02 07:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_auto_20220201_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.IntegerField(default=0, verbose_name='Сумма'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='is_buy',
            field=models.BooleanField(default=True, verbose_name='Покупка? False - возврат'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='type',
            field=models.CharField(max_length=20, verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='user',
            name='pay_summ',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='К выплате'),
        ),
        migrations.AlterField(
            model_name='user',
            name='total_amount',
            field=models.IntegerField(default=0, verbose_name='Всего картин'),
        ),
        migrations.AlterField(
            model_name='user',
            name='total_in_store',
            field=models.IntegerField(default=0, verbose_name='Заложено картин'),
        ),
        migrations.AlterField(
            model_name='user',
            name='total_summ',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Сумма куртин'),
        ),
        migrations.AlterField(
            model_name='withdrawalrequest',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='withdrawal_requests', to=settings.AUTH_USER_MODEL),
        ),
    ]
