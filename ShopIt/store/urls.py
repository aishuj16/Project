from django.contrib import admin
from django.urls import path
from .views.login import Login
from.views.signup import Signup
from.views.home import index

urlpatterns = [
    path('', index , name='index'),
    path('signup',Signup.as_view(), name ='signup'),
    path('login', Login.as_view(), name ='login')
]
