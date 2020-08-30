from django.urls import path
from . import views

app_name = 'enquetes'
urlpatterns = [
    path('bemvindo/', views.bemvindo, name="bemvindo"),
    path('enquete/<int:id_enquete>/', views.enquete, name="enquete"),
]
