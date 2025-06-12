from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('authorize', views.HomeView.as_view(), name='authorize'),
    path('login', views.LoginInterfaceView.as_view(), name='login'),
    path('logout', LogoutView.as_view(template_name='home/logout.html'), name='logout'),
    path('signup', views.SignUpView.as_view(), name='signup'),
]