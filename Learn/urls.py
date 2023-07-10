from django.contrib import admin
from django.urls import path, include
from Learn import views
urlpatterns = [
    path('',views.Home,name="Home"),
    path('signup',views.signup,name="signup"),
    path('signin',views.signin,name="signin")
]
