# Generated by Django 3.2.7 on 2022-01-21 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Item', '0005_alter_collection_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_nft',
            field=models.BooleanField(default=False, verbose_name='NFT'),
        ),
    ]
