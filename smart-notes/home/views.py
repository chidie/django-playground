from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy    
from django.views.generic.edit import CreateView

class SignUpView(CreateView):
    """
    Class-based view for user registration in the SmartNote application.
    """
    form_class = UserCreationForm
    template_name = 'home/signup.html'
    success_url = reverse_lazy('login')  # Redirect to login page after successful registration

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = datetime.now()
        return context

class HomeView(TemplateView):
    """
    Class-based view for rendering the home page of the SmartNote application.
    """
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.now()}

class AuthorizeView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorize.html'
    login_url = '/admin'

class LoginInterfaceView(LoginView):
    """
    Class-based view for handling user login.
    """
    template_name = 'home/login.html'
    # redirect_authenticated_user = True  # Redirect to home if user is already authenticated

    # def get_success_url(self):
    #     return self.get_redirect_url() or '/notes/list'  # Redirect to notes list after login
