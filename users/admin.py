"""
admin.py

Register the NewUser custom model on the admin portal.
"""

from django.contrib import admin
from .models import NewUser

# Register your models here.
admin.site.register(NewUser)
