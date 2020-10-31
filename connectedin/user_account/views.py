from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import RegisterUserForm, LoginUserForm
from .models import UserAccount
from core.models import Profile
from django.http import HttpResponseNotAllowed, HttpResponse


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
            profile.save()
            return redirect('/')
        return render(request, self.template_name, {'form':form})


class LoginView(View):
    form_class = LoginUserForm
    template_name = 'user_account/login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        form = self.form_class()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            if user:
                return redirect(request.GET.get('next', '/'))
            form.append_error('Username and Password Invalid!')
        return render(request, self.template_name, {'form':form})


class LogoutView(View):
    def get(self, request):
        
        return HttpResponseNotAllowed(permitted_methods=['POST'])

    def post(self, request):
        logout(request)
        return redirect('/')