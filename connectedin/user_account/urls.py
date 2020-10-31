from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RegisterView, LoginView
from .forms import LoginUserForm

app_name = "user_account"

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name='register')
]
