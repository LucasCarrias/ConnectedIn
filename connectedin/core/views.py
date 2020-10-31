from django.shortcuts import render, get_object_or_404
from .models import Profile, Invitation
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    profiles = Profile.objects.all().exclude(user=request.user)
    return render(request,
                  "core/home.html",
                  {'profiles': profiles})

@login_required
def profile(request, profile_slug):
    profile = get_object_or_404(Profile, slug=profile_slug)
    context = {'profile': profile}
    current_user = get_object_or_404(Profile, id=1)
    return render(request,
                  'core/profile.html',
                  {'profile': profile})

@login_required
@require_POST
def invite(request, profile_slug):
    profile = get_object_or_404(Profile, slug=profile_slug)
    dummy_user = get_object_or_404(Profile, id=1)
    Invitation.objects.create(user_from=dummy_user, user_to=profile)
    return render(request,
                  'core/profile.html',
                  {'profile': profile,
                   'message': 'Invitation Sent'})