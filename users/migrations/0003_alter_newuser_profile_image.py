# Generated by Django 5.1.6 on 2025-02-18 19:27

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_newuser_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='profile_image',
            field=cloudinary.models.CloudinaryField(default='profile_image', max_length=255, verbose_name='profile_image'),
        ),
    ]
