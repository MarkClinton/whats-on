# Generated by Django 5.1.6 on 2025-02-17 23:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_rename_comments_comment'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EventAttendees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rsvp', models.IntegerField(choices=[(0, 'Not Going'), (1, 'Going'), (2, 'Maybe')], default=0)),
                ('is_blocked', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('attendee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendee', to=settings.AUTH_USER_MODEL)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attending', to='event.event')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
