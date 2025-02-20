from django.shortcuts import render
from django.views import generic
from .models import Event

class EventList(generic.ListView):
    queryset = Event.objects.all()  # pylint: disable=no-member
    template_name = "event/search.html"

def event_create(request):
    queryset = Event.objects.all()  # pylint: disable=no-member

    return render(
        request,
        "event/create.html",
        {
            "event": queryset,
        },
    )

def event_hosting(request):
    queryset = Event.objects.all()  # pylint: disable=no-member

    return render(
        request,
        "event/hosting.html",
        {
            "event": queryset,
        },
    )

def event_attending(request):
    queryset = Event.objects.all()  # pylint: disable=no-member

    return render(
        request,
        "event/attending.html",
        {
            "event": queryset,
        },
    )
