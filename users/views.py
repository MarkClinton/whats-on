from django.shortcuts import render
from django.contrib import messages
from .models import NewUser
from .forms import ProfileForm

def get_profile(request):

    user_profile = NewUser.objects.get(email=request.user.email)

    if request.method == "POST":
        profile_form = ProfileForm(data=request.POST, instance=user_profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Profile Successfully Updated'
            )

    profile_form = ProfileForm(instance=user_profile)
    return render(
        request,
        "users/profile.html",
        {
            "profile_form": profile_form,
        },
    )
