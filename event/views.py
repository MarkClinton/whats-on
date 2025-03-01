from datetime import date
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.views.generic.edit import FormMixin
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from .models import Event, EventAttendees
from.forms import EventForm, SearchForm

class EventList(generic.ListView, FormMixin):
    today = date.today()
    queryset = Event.objects.filter(date__gte=today)  # pylint: disable=no-member
    template_name = "event/search.html"
    paginate_by = 10
    form_class = SearchForm

def event_detail(request, event_id):
    event_query = Event.objects.all() # pylint: disable=no-member
    attendee_count = EventAttendees.objects.filter(event=event_id).count() # pylint: disable=no-member
    event = get_object_or_404(event_query, id=event_id)

    return render(
        request,
        "event/event_detail.html",
        {
            "event": event,
            "attendee_count": attendee_count,
        }
    )

def event_create(request):

    if request.method == "POST":
        event_form = EventForm(data=request.POST, files=request.FILES)
        if event_form.is_valid():
            event = event_form.save(commit=False)
            event.host = request.user
            event.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Event Successfully Created'
            )
            return HttpResponseRedirect(reverse('event_create'))
        return render(
        request,
        "event/create.html",
        {
            "event_form": event_form,
        },
    )

    event_form = EventForm()
    return render(
        request,
        "event/create.html",
        {
            "event_form": event_form,
        },
    )

def event_edit(request, event_id):
    pass

def event_delete(request, event_id):

    event_query = Event.objects.all() # pylint: disable=no-member
    event = get_object_or_404(event_query, id=event_id)

    if event.host == request.user:
        event.delete()
        messages.add_message(request, messages.SUCCESS, 'Event successfully deleted.')
    else:
        messages.add_message(request, messages.ERROR, 'You cant delete someone elses event')

    return HttpResponseRedirect(reverse('event_hosting'))


def event_hosting(request):

    events = Event.objects.filter(host=request.user) # pylint: disable=no-member
    # Filter for 2 batches of events: future events and past events
    # today = date.today()
    # future_events = events.filter(date__gte=today)
    # past_events = events.filter(date__lt=today)

    paginator = Paginator(events, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "event/hosting.html",
        {
            "events": events,
            "page_obj": page_obj,
        },
    )

def event_attending(request):
    attending_events = EventAttendees.objects.select_related("event").filter(attendee=request.user) # pylint: disable=no-member
    paginator = Paginator(attending_events, 9)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "event/attending.html",
        {
            "attending_events": attending_events,
            "page_obj": page_obj,
        },
    )
