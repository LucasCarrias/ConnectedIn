from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('', views.home, name="home"),
    path('profile/<slug:profile_slug>/', views.profile, name="profile"),
    path('profile/<slug:profile_slug>/invite', views.invite, name="invite"),
]
