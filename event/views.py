from datetime import date
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.views.generic.edit import FormMixin
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Event, EventAttendees
from.forms import EventForm, SearchForm

class EventList(LoginRequiredMixin, generic.ListView, FormMixin):
    today = date.today()
    queryset = Event.objects.filter(date__gte=today)  # pylint: disable=no-member
    ordering = ['date']
    template_name = "event/event_search.html"
    paginate_by = 10
    form_class = SearchForm

def event_detail(request, event_id):
    event_query = Event.objects.all() # pylint: disable=no-member
    event = get_object_or_404(event_query, id=event_id)

    attendee_list = EventAttendees.objects.select_related('attendee').filter(event=event_id) # pylint: disable=no-member
    attendee_count = attendee_list.count()
    is_user_attending = attendee_list.filter(attendee=request.user).exists()

    capacity = event.limit is not None and attendee_count >= event.limit

    today = date.today()
    in_the_past = event.date < today

    return render(
        request,
        "event/event_detail.html",
        {
            "event": event,
            "is_user_attending": is_user_attending,
            "attendee_count": attendee_count,
            "capacity": capacity,
            "in_the_past": in_the_past,
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
            return HttpResponseRedirect(reverse('event_hosting'))
        return render(
        request,
        "event/create_event.html",
        {
            "event_form": event_form,
        },
    )

    event_form = EventForm()
    return render(
        request,
        "event/create_event.html",
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
        return render(
        request,
        "event/event_edit.html",
        {
            "event_form": event_form,
        },
    )

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
    today = date.today()
    future_events = events.filter(date__gte=today)
    past_events = events.filter(date__lt=today)

    is_events_none = future_events.count() == 0
    is_past_events_none = past_events.count() == 0

    paginator = Paginator(future_events, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "event/event_hosting.html",
        {
            "page_obj": page_obj,
            "past_events": past_events,
            "is_events_none": is_events_none,
            "is_past_events_none": is_past_events_none,
        },
    )

def event_attending(request):

    attending_events = Event.objects.filter(attending__attendee=request.user) # pylint: disable=no-member

    today = date.today()
    future_events = attending_events.filter(date__gte=today)
    past_events = attending_events.filter(date__lt=today)

    is_events_none = future_events.count() == 0
    is_past_events_none = past_events.count() == 0

    paginator = Paginator(future_events, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "event/event_attending.html",
        {
            "page_obj": page_obj,
            "past_events": past_events,
            "is_events_none": is_events_none,
            "is_past_events_none": is_past_events_none,
        },
    )

def attend_event(request, event_id):
    event = Event.objects.get(id=event_id) # pylint: disable=no-member
    event.add_user_to_event(user=request.user)
    return HttpResponseRedirect(reverse('event_attending'))

def remove_attend_event(request, event_id):
    event = EventAttendees.objects.get(event=event_id, attendee=request.user) # pylint: disable=no-member
    event.delete()
    return HttpResponseRedirect(reverse('event_attending'))
