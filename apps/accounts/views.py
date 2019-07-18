from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView
from django.contrib.auth.views import LoginView, AuthenticationForm, PasswordChangeView, PasswordResetView
from .forms import RegistrationForm

# Create your views here.
class LoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm


class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name= 'signup.html'
    success_url = '/'
