# Generated by Django 4.2.7 on 2023-12-12 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0007_addpost_view_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Content', models.TextField()),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('Name', models.CharField(max_length=80)),
                ('Email', models.EmailField(max_length=254)),
                ('Author', models.CharField(max_length=200)),
                ('Post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='add_posts', to='jobapp.addpost')),
            ],
        ),
    ]
