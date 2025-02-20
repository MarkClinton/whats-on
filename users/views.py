from django.shortcuts import render
from .models import NewUser

def get_profile(request):
    queryset = NewUser.objects.all()  # pylint: disable=no-member

    return render(
        request,
        "users/profile.html",
        {
            "profile": queryset,
        },
    )
