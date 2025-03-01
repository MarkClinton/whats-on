from django.urls import path
from . import views

urlpatterns = [
    path('<int:event_id>/', views.event_detail, name='event_detail'),
    path('attending/', views.event_attending, name='event_attending'),
    path('hosting/', views.event_hosting, name='event_hosting'),
    path('create/', views.event_create, name='event_create'),
    path('', views.EventList.as_view(), name='event_search'),
    path('<int:event_id>/edit_event/',
        views.event_edit, name='event_edit'),
    path('<int:event_id>/delete_event/',
        views.event_delete, name='event_delete'),
]
