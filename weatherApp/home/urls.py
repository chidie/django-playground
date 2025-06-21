from django.urls import path
from .views import CheckWeatherView, LoginInterface, signup, weather_report
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', LoginInterface.as_view(), name='login'),
    path('check_weather/', CheckWeatherView.as_view(), name='check_weather'),
    path('login/', LoginInterface.as_view(), name='login'),
    path('weather_report/', weather_report, name='weather_report'),
    path('signup/', signup, name='signup'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]