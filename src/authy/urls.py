from django.contrib import admin
from django.urls import path
from .views import RegisterPageView, LoginPageView, LogoutPageView


app_name = 'authy'

urlpatterns = [
    path('register/', RegisterPageView.as_view(), name='register'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('logout/', LogoutPageView.as_view(next_page='authy:login'), name='logout'),
]
