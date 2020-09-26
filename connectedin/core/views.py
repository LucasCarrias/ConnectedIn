from django.shortcuts import render, get_object_or_404
from .models import Profile, Invitation
from django.views.decorators.http import require_POST


def home(request):
    profiles = Profile.objects.all()
    return render(request,
                  "core/home.html",
                  {'profiles': profiles})


def profile(request, profile_slug):
    profile = get_object_or_404(Profile, slug=profile_slug)
    return render(request,
                  'core/profile.html',
                  {'profile': profile})


@require_POST
def invite(request, profile_slug):
    profile = get_object_or_404(Profile, slug=profile_slug)
    dummy_user = get_object_or_404(Profile, id=1)
    Invitation.objects.create(user_from=dummy_user, user_to=profile)
    return render(request,
                  'core/profile.html',
                  {'profile': profile,
                   'message': 'Invitation Sent'})