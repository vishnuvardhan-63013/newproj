# Generated by Django 4.2.7 on 2023-12-01 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submit',
            name='jobtitle',
        ),
    ]
