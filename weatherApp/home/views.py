from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from .forms import CityForm, LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
import urllib.request
import json

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'home/signup.html', {'form': form})

class LoginInterface(LoginView):
    template_name = 'home/login.html'
    authentication_form = LoginForm

class LogoutView(TemplateView):
    template_name = 'home/logout.html'


class CheckWeatherView(LoginRequiredMixin, FormView):
    template_name = 'home/check_weather.html'
    form_class = CityForm

    def form_valid(self, form):
        city = form.cleaned_data['city']
        return self.render_to_response(self.get_context_data(form=form, city=city))

@login_required
def weather_report(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            API_KEY = 'ed3ef0c75bf8400e7de2a1854cfd3b47'
            response = urllib.request.urlopen(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric').read()
            weather_data = json.loads(response)
            return render(request, 'home/weather_report.html', {'data': weather_data})
    else:
        form = CityForm()
        return render(request, 'home/weather_report.html', {'data': None})