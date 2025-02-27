from django import forms
from cloudinary.forms import CloudinaryFileField
from .models import NewUser


class ProfileForm(forms.ModelForm):

    about = forms.CharField(widget=forms.Textarea(attrs={'rows' : '3'}))
    profile_image = CloudinaryFileField()

    class Meta:
        model = NewUser
        fields = (
            'first_name', 'last_name', 'email', 'profile_image', 'location', 'phone_number', 'about'
        )
