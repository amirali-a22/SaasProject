from django.urls import path
from .views import Home, SignUpV, LoginV, LogoutV

app_name = 'core'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('signup/', SignUpV.as_view(), name='signup'),
    path('login/', LoginV.as_view(), name='login'),
    path('logout/', LogoutV.as_view(), name='logout'),
]
