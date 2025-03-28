from django.urls import path
from . import views

urlpatterns = [
    path('', views.check_pesel, name='check_pesel'),
]