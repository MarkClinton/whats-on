from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from .models import Event
from.forms import EventForm

class EventList(generic.ListView):
    queryset = Event.objects.all()  # pylint: disable=no-member
    template_name = "event/search.html"

def event_create(request):

    if request.method == "POST":
        event_form = EventForm(data=request.POST)
        if event_form.is_valid():
            event = event_form.save(commit=False)
            event.host = request.user
            event.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Event Successfully Created'
            )

    event_form = EventForm()
    return render(
        request,
        "event/create.html",
        {
            "event_form": event_form,
        },
    )

def event_hosting(request):
    try:
        events = Event.objects.filter(host=request.user) # pylint: disable=no-member
    except Event.DoesNotExist: # pylint: disable=no-member
        events = None

    return render(
        request,
        "event/hosting.html",
        {
            "events": events,
        },
    )

def event_attending(request):
    events = Event.objects.all()  # pylint: disable=no-member

    return render(
        request,
        "event/attending.html",
        {
            "events": events,
        },
    )
