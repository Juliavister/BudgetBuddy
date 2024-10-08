# Generated by Django 4.2.6 on 2024-03-19 16:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_uploadphoto_alter_addmoney_info_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadphoto',
            name='uploaded_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='uploadphoto',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
