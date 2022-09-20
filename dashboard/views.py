from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class DashboardV(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/dashboard.html'
