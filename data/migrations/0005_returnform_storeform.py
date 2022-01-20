# Generated by Django 3.2.7 on 2022-01-18 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0006_order_is_pay'),
        ('data', '0004_contactform_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Текст')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Order.orderitem')),
            ],
        ),
        migrations.CreateModel(
            name='ReturnForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Текст')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Order.orderitem')),
            ],
        ),
    ]