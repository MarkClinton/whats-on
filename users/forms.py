from django import forms
from cloudinary.forms import CloudinaryFileField
from phonenumber_field.formfields import PhoneNumberField
from .models import NewUser


class ProfileForm(forms.ModelForm):

    TEL_MESSAGE ='Incorrect format. Use an Irish number. e.g. (087) 456 7890.'

    about = forms.CharField(widget=forms.Textarea(attrs={'rows' : '3'}))
    phone_number = PhoneNumberField(
        widget=forms.TextInput(attrs={'placeholder': 'Irish Phone Numbers Only'}),
        required=False,
        region="IE"
    )
    phone_number.error_messages['invalid'] = TEL_MESSAGE
    profile_image = CloudinaryFileField()

    class Meta:
        model = NewUser
        fields = (
            'first_name', 'last_name', 'email', 'profile_image', 'location', 'phone_number', 'about'
        )
