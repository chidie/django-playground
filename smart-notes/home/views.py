from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required

def home(request):
    """
    Render the home page of the SmartNote application.
    """
    return render(request, 'home/welcome.html', {'today': datetime.now()})

@login_required(login_url='/admin')
def authorize(request):
    """
    Render the authorization page for the SmartNote application.
    """
    return render(request, 'home/authorize.html', {'today': datetime.now()})
    # return HttpResponse("<h1>Authorization Page</h1><p>Please authorize your account.</p>")
