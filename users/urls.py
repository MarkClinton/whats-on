from django.urls import path
from . import views

urlpatterns = [
    path('user', views.get_profile, name='user_profile'),
]
