"""ServiceDesk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth,Group
from django.http import HttpResponse
from django.views.generic.base import RedirectView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views
from django.shortcuts import render, redirect
# def my_view(request):
# 	if request.user.is_superuser:
def sample_view(request):
	print(request.user.id )
	return redirect    
# 		return redirect('temp')
    
# def temp(request):
# 	return HttpResponse("K")
# @login_required
# def index(request):
#     group = request.user.groups.filter(user=request.user)[0]
#     if group.name=="employees":
#         return HttpResponseRedirect(reverse('admin'))
#     elif group.name=="teamLeader":
#         return HttpResponseRedirect(reverse('manager'))
  
urlpatterns = [
    		path('super', admin.site.urls,name='super'),
    		# path('view',my_view,name='view'),
    		path('sample_view',sample_view,name='temp')
    		# path('', RedirectView.as_view(url='login/?next=/admin/', permanent=True))

    		# path('home',home),
    		 # path('login/', views.loginView.as_view(), name='login')

    		
    		]