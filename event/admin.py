from django.contrib import admin
from .models import Event, Comments, Category

# Register your models here.
admin.site.register(Event)
admin.site.register(Comments)
admin.site.register(Category)
