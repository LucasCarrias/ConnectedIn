from django.shortcuts import render
from .models import Profile, Invitation


def home(request):
    profiles = Profile.objects.all()
    return render(request,
                  "core/home.html",
                  {'profiles': profiles})
