# Generated by Django 3.2.7 on 2021-09-28 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Item', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Статус')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='image_alt',
            field=models.ImageField(blank=True, null=True, upload_to='item/full', verbose_name='Большое изображение'),
        ),
        migrations.AddField(
            model_name='item',
            name='image_alt_thumb',
            field=models.ImageField(blank=True, null=True, upload_to='item/thumb', verbose_name='Маленькое изображение'),
        ),
        migrations.AddField(
            model_name='item',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Item.itemstatus'),
        ),
    ]
