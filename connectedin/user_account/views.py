from django.shortcuts import render,redirect
from django.views import View
from .forms import RegisterUserForm
from .models import UserAccount
from core.models import Profile


class RegisterView(View):
    form_class = RegisterUserForm
    template_name = 'user_account/register.html'
    
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            user = UserAccount.objects.create_user(
                username = form_data['username'],
                email = form_data['email'],
                password= form_data['password1']
            )
            profile = Profile(
                user=user,
                name=form_data['username']
            )
            return redirect('/')
        return render(request, self.template_name, {'form':form})