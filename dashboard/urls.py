from django.urls import path
from .views import DashboardV

app_name = 'dashboard'

urlpatterns = [
    path('dashboard/', DashboardV.as_view(), name='dashboard'),
]
