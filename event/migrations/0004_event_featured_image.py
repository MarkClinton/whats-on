# Generated by Django 5.1.6 on 2025-02-18 19:23

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_eventattendees'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='event_image', max_length=255, verbose_name='image'),
        ),
    ]
