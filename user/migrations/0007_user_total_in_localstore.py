# Generated by Django 3.2.7 on 2022-01-26 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_user_pay_summ'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='total_in_localstore',
            field=models.IntegerField(default=0),
        ),
    ]
