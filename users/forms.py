from django import forms
from django.contrib.auth import get_user_model
from django.forms import ValidationError
from cloudinary.forms import CloudinaryFileField
from phonenumber_field.formfields import PhoneNumberField
from allauth.account.forms import SignupForm
from .models import NewUser

User = get_user_model()


class ProfileForm(forms.ModelForm):

    TEL_MESSAGE = 'Incorrect format. Use an Irish number. e.g. (087) 456 7890.'
    TEL_PLACEHOLDER = 'Irish Phone Numbers Only'

    about = forms.CharField(widget=forms.Textarea(attrs={'rows': '3'}))
    phone_number = PhoneNumberField(
        widget=forms.TextInput(attrs={'placeholder': TEL_PLACEHOLDER}),
        required=False,
        region="IE"
    )
    phone_number.error_messages['invalid'] = TEL_MESSAGE
    profile_image = CloudinaryFileField()

    class Meta:
        model = NewUser
        fields = (
            'first_name',
            'last_name',
            'email',
            'profile_image',
            'location',
            'phone_number',
            'about'
        )


class CustomSignupForm(SignupForm):
    """
    Declares a custom sign up form inheriting from AllAuths
    SignupForm

    :param SignupForm: AllAuth Signup Form
    """
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("A user with this email already exists.")
        return email
