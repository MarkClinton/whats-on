from django.shortcuts import render, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import NewUser
from .forms import ProfileForm


@login_required
def get_profile(request):

    user_profile = NewUser.objects.get(email=request.user.email)

    if request.method == "POST":
        profile_form = ProfileForm(
            data=request.POST,
            files=request.FILES,
            instance=user_profile
        )
        if profile_form.is_valid():
            profile_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Profile Successfully Updated'
            )
            return HttpResponseRedirect(reverse('user_profile'))
        return render(
            request,
            "users/profile.html",
            {
                "profile_form": profile_form,
            },
        )

    profile_form = ProfileForm(instance=user_profile)
    return render(
        request,
        "users/profile.html",
        {
            "profile_form": profile_form,
        },
    )
