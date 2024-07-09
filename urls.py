"""
URL configuration for myproject3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# app1/urls.py

from django.contrib import admin
from django.urls import path, include
from app1 import views
from app1.views import google_oauth_login, google_oauth_callback
from app1.views import MyTokenObtainPairView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', views.login_view, name='api_login'),
    path('api/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/register/', views.register_view, name='api_register'),
    path('login/google/', google_oauth_login, name='google_oauth_login'),
    path('complete/google-oauth2/', google_oauth_callback, name='google_oauth_callback'),
    path('auth/', include('social_django.urls', namespace='social')), 
    
]


