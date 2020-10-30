from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RegisterView
from .forms import LoginUserForm

app_name = "user_account"

urlpatterns = [
    path('login/', 
         auth_views.LoginView.as_view(template_name="user_account/login.html", 
                                      extra_context={'form':LoginUserForm},
                                      redirect_field_name="/"),
         name="login"),
    path('register/', RegisterView.as_view(), name='register')
]
