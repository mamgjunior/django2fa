from django.shortcuts import render
from . forms import LoginForm
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request, template_name='accounts/dashboard.html'):
    return render(request, template_name, {'section': 'dashboard'})