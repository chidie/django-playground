from django.urls import path
from . import views

urlpatterns = [
    path('home', views.HomeView.as_view(), name='home'),
    path('authorize', views.HomeView.as_view(), name='authorize'),
]