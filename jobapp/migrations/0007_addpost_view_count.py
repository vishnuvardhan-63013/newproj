# Generated by Django 4.2.7 on 2023-12-11 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0006_alter_addpost_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='addpost',
            name='view_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
