from django import forms
from .models import NewUser


class ProfileForm(forms.ModelForm):

    about = forms.CharField(widget=forms.Textarea(attrs={'rows' : '3'}))
    class Meta:
        model = NewUser
        fields = (
            'first_name', 'last_name', 'email', 'location', 'phone_number', 'about'
        )
