from django import forms

class PostForm(forms.Form):
    body = forms.CharField(required=True)
