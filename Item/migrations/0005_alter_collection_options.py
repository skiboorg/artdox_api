# Generated by Django 3.2.7 on 2021-10-10 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Item', '0004_auto_20211010_1039'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collection',
            options={'ordering': ['order']},
        ),
    ]
