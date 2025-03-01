from django.urls import path
from . import views

urlpatterns = [
    path('<int:event_id>/', views.event_detail, name='event_detail'),
    path('attending/', views.event_attending, name='event_attending'),
    path('hosting/', views.event_hosting, name='event_hosting'),
    path('create/', views.event_create, name='event_create'),
    path('', views.EventList.as_view(), name='event_search'),
]
