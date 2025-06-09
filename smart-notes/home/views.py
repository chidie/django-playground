from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class HomeView(TemplateView):
    """
    Class-based view for rendering the home page of the SmartNote application.
    """
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.now()}

class AuthorizeView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorize.html'
    login_url = '/admin'

