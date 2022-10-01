from django.urls import path
from .views import DashboardV,Settings

app_name = 'dashboard'

urlpatterns = [
    path('dashboard/', DashboardV.as_view(), name='dashboard'),
    path('settings/<int:pk>/', Settings.as_view(), name='settings'),
]
