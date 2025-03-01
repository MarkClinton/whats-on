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
    ordering = ['date']
    template_name = "event/search.html"
    paginate_by = 10
    form_class = SearchForm

def event_detail(request, event_id):
    event_query = Event.objects.all() # pylint: disable=no-member
    event = get_object_or_404(event_query, id=event_id)

    attendee_list = EventAttendees.objects.filter(event=event_id).select_related('attendee') # pylint: disable=no-member
    attendee_count = attendee_list.count()
    user_attending = attendee_list.filter(attendee=request.user).exists()

    return render(
        request,
        "event/event_detail.html",
        {
            "event": event,
            "user_attending": user_attending,
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
    event_query = Event.objects.all() # pylint: disable=no-member
    event = get_object_or_404(event_query, id=event_id)

    if request.method == "POST":
        event_form = EventForm(data=request.POST, files=request.FILES, instance=event)
        if event_form.is_valid():
            event_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Event Successfully Updated'
            )
            return HttpResponseRedirect(reverse('event_detail', args=[event_id]))

    event_form = EventForm(instance=event)
    return render(
        request,
        "event/event_edit.html",
        {
            "event_form": event_form,
        },
    )

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

def attend_event(request, event_id):
    event = Event.objects.get(id=event_id) # pylint: disable=no-member
    event.add_user_to_event(user=request.user)
    return HttpResponseRedirect(reverse('event_detail', args=[event_id]))
