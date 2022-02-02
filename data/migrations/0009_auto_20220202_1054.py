# Generated by Django 3.2.7 on 2022-02-02 07:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('data', '0008_auto_20220201_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact_requests', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='returnform',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='return_requests', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='storeform',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='store_requests', to=settings.AUTH_USER_MODEL),
        ),
    ]