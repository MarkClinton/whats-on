from django.shortcuts import render, reverse
from django.views import generic
from django.views.generic.edit import FormMixin
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from .models import Event, EventAttendees
from.forms import EventForm, SearchForm

class EventList(generic.ListView, FormMixin):
    queryset = Event.objects.all()  # pylint: disable=no-member
    template_name = "event/search.html"
    paginate_by = 10
    form_class = SearchForm

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

def event_hosting(request):

    events = Event.objects.filter(host=request.user) # pylint: disable=no-member
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
