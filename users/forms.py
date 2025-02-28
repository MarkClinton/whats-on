from django import forms
from cloudinary.forms import CloudinaryFileField
from phonenumber_field.formfields import PhoneNumberField
from .models import NewUser


class ProfileForm(forms.ModelForm):

    about = forms.CharField(widget=forms.Textarea(attrs={'rows' : '3'}))
    phone_number = PhoneNumberField(
        widget=forms.TextInput(attrs={'placeholder': 'Format: (123) 4567 890'}),
        required=False,
        region="IE"
    )
    phone_number.error_messages['invalid'] = 'Incorrect Format. Use Format (123)-456-7890.'
    profile_image = CloudinaryFileField()

    class Meta:
        model = NewUser
        fields = (
            'first_name', 'last_name', 'email', 'profile_image', 'location', 'phone_number', 'about'
        )
