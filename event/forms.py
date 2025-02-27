from django import forms
from .models import Event


class EventForm(forms.ModelForm):

    description = forms.CharField(widget=forms.Textarea(attrs={'rows' : '3'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'type' : 'date'}), label='Event Date')
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={'type' : 'time'}))
    end_time = forms.TimeField(widget=forms.TimeInput(attrs={'type' : 'time'}))

    class Meta:
        model = Event
        fields = (
            'event_title', 'description', 'category', 'event_image', 'date', 
            'start_time', 'end_time', 'location', 'limit', 'enable_comments'
        )

class SearchForm(forms.Form):

    description = forms.CharField(widget=forms.Textarea(attrs={'rows' : '3'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'type' : 'date'}), label='Event Date')
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={'type' : 'time'}))
    end_time = forms.TimeField(widget=forms.TimeInput(attrs={'type' : 'time'}))

    class Meta:
        model = Event
        fields = (
            'event_title', 'description', 'category', 'event_image', 'date', 
            'start_time', 'end_time', 'location', 'limit', 'enable_comments'
        )
        