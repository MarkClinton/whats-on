# Generated by Django 5.1.6 on 2025-02-18 19:27

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_event_featured_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='featured_image',
        ),
        migrations.AddField(
            model_name='event',
            name='event_image',
            field=cloudinary.models.CloudinaryField(default='event_image', max_length=255, verbose_name='event_image'),
        ),
    ]
