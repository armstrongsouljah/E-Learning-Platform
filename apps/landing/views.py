from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class LandingView(LoginRequiredMixin, TemplateView):
    template_name = 'landing.html'
    
