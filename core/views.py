from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib import messages


class Home(TemplateView):
    template_name = 'core/home.html'


class LoginV(LoginView):
    template_name = 'core/login.html'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()
        messages.success(request=self.request, message='u logged in successfully!', )
        return super().form_valid(form)


class LogoutV(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.error(request=request, message='u logged out successfully!', )
        return super().dispatch(request, *args, **kwargs)


class SignUpV(FormView):
    template_name = 'core/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('core:home')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()
        messages.success(request=self.request, message='u signed up successfully!', )
        return super().form_valid(form)
