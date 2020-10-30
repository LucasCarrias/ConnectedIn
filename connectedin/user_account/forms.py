from django import forms
from django.contrib.auth.models import User


class LoginUserForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)


class RegisterUserForm(forms.Form):
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, required=True)
    birth_day = forms.DateField(required=True, widget=forms.DateInput)

    def is_valid(self):
        valid = super(RegisterUserForm, self).is_valid()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        username = self.cleaned_data['username']
        if password1 != password2:
            self.append_error('Passwords doesn\'t match')
            valid = False
        if User.objects.filter(username=username).exists():
            self.append_error('Username already taken')
            valid = False
        
        return valid

    def append_error(self, message):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS,
                                        forms.utils.ErrorList())
        errors.append(message)