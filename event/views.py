from django.shortcuts import render
from django.views import generic
from .models import Event

class EventList(generic.ListView):
    queryset = Event.objects.all()  # pylint: disable=no-member
    template_name = "event/index.html"
