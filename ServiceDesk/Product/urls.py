from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from . import views
from . import admin


urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # path('agent/',views.agent, name='agent'),
    # path('',views.home, name='home'),
    path('data',admin.access_session_data,name='data')
    
]