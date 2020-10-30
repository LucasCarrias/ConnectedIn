from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import LoginUser

app_name = "user_account"

urlpatterns = [
    path('login/', 
         auth_views.LoginView.as_view(template_name="user_account/login.html", 
                                      extra_context={'form':LoginUser},
                                      redirect_field_name="/"),
         name="login")
]
