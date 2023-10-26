from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import BaseRegisterView, CodeRandomView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('signup/', BaseRegisterView.as_view(template_name='signup.html'), name='signup'),
    path('coder/<str:user>', CodeRandomView.as_view(), name='code'),
    path('in_coder/<str:user>', CodeRandomView.as_view(), name='in_code'),
]
