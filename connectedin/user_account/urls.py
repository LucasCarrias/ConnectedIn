from django.urls import path
from django.contrib.auth import logout
from .views import RegisterView, LoginView, LogoutView
from .forms import LoginUserForm

app_name = "user_account"

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', RegisterView.as_view(), name='register')
]
