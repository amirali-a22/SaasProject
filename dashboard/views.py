from django.shortcuts import render
from django.views.generic import View, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages
from django import forms
from userprofile.conts import ChoicePlans


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

    def get_context_data(self, **kwargs):
        context = super(Settings, self).get_context_data(**kwargs)
        plans = self.request.user.profile.plan if self.request.user.profile.plan else None
        context['form'].fields.update({'plans': forms.ChoiceField(choices=ChoicePlans.CHOICE_PLANS, initial=plans)})
        return context

    def post(self, request, *args, **kwargs):
        user = request.user
        user.profile.plan = request._post['plans']
        user.profile.save()
        return super(Settings, self).post(request, *args, **kwargs)
