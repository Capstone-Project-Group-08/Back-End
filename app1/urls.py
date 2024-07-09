from django.urls import path
from app1.views import forgot_password

urlpatterns = [
    path('forgot-password/', forgot_password, name='forgot_password'),
]
