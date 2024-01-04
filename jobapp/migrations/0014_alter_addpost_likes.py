# Generated by Django 4.2.7 on 2023-12-28 03:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobapp', '0013_addpost_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addpost',
            name='likes',
            field=models.ManyToManyField(blank=True, default=None, related_name='postlike', to=settings.AUTH_USER_MODEL),
        ),
    ]
