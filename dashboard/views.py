from django.shortcuts import render
from django.views.generic import View, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages


class DashboardV(LoginRequiredMixin, View):
    template_name = 'dashboard/dashboard.html'

    def get(self, request, *args, **kwargs):
        bookmarks = request.user.bookmarks.all().order_by('-created_at')[:5]
        categories = request.user.categories.all().order_by('-created_at')[:5]

        context = {
            'bookmarks': bookmarks,
            'categories': categories,
        }
        return render(request, self.template_name, context)


class Settings(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'dashboard/settings.html'
    fields = ['username', 'first_name', 'last_name', 'email']

    def get_success_url(self):
        messages.success(request=self.request, message='ur profile updated successfully!')
        return reverse('dashboard:settings', args=[self.request.user.pk])
