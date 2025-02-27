from django import forms
from cloudinary.forms import CloudinaryFileField
from .models import Event


class EventForm(forms.ModelForm):

    description = forms.CharField(widget=forms.Textarea(attrs={'rows' : '3'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'type' : 'date'}), label='Event Date')
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={'type' : 'time'}))
    end_time = forms.TimeField(widget=forms.TimeInput(attrs={'type' : 'time'}))
    event_image = CloudinaryFileField()

    class Meta:
        model = Event
        fields = (
            'event_title', 'description', 'category', 'event_image', 'date', 
            'start_time', 'end_time', 'location', 'limit', 'enable_comments'
        )

class SearchForm(forms.ModelForm):

    CHOICES = (
        (1, 'Today'),
        (2, 'Tomorrow'),
        (3, 'This Weekend'),
        (4, 'Next Week'),
    )

    when = forms.ChoiceField(choices=CHOICES)
    date = forms.DateField(widget=forms.DateInput(attrs={'type' : 'date'}), label='Pick a date')
    location = forms.CharField()

    class Meta:
        model = Event
        fields = (
            'when', 'date', 'location', 'category',
        )
        