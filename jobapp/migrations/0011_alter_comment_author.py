# Generated by Django 4.2.7 on 2023-12-14 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0010_rename_post_comment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='Author',
            field=models.CharField(max_length=120),
        ),
    ]