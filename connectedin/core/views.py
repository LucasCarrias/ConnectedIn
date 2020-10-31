from django.shortcuts import render, get_object_or_404
from .models import Profile, Invitation, Post
from .forms import PostForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

@login_required
def home(request):
    current_profile = Profile.objects.get(user=request.user)
    profiles = Profile.objects.all().exclude(user=request.user)
    invitations = Invitation.objects.filter(user_to=current_profile).all()
    return render(request,
                  "core/home.html",
                  {'profiles': profiles,
                   'invitations': current_profile.invitations.filter(status="waiting"),
                   'contacts': current_profile.connections,
                   'timeline': current_profile.timeline}
                   )

@login_required
def profile(request, profile_slug):
    profile = get_object_or_404(Profile, slug=profile_slug)
    context = {'profile': profile}
    current_profile = Profile.objects.get(user=request.user)
    if profile in current_profile.connections:
        context['message'] = 'Is your connection'
    return render(request,
                  'core/profile.html',
                  context=context
                  )

@login_required
@require_POST
def invite(request, profile_slug):
    target_profile = get_object_or_404(Profile, slug=profile_slug)
    current_profile = Profile.objects.get(user=request.user)
    Invitation.objects.create(user_from=current_profile, user_to=target_profile)
    return render(request,
                  'core/profile.html',
                  {'profile': profile,
                   'message': 'Invitation Sent'})

@login_required
@require_POST
def accept_invite(request, id):
    invitation = Invitation.objects.get(id=id)
    invitation.status = "accepted"
    invitation.save()
    return redirect("/")


@login_required
def create_post(request):
    if request.method == "POST":
        current_profile = Profile.objects.get(user=request.user)
        form = PostForm(request.POST)
        if form.is_valid():
            Post(body=form.cleaned_data['body'], profile=current_profile).save()
            return redirect('/')
        else:
            return redirect('post/create')
    else:
        return render(request, 'core/posts/create.html', {'form': PostForm()})