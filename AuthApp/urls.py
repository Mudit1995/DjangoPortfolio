from django.urls import path
from AuthApp import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.hanlogin, name='hanlogin'),
    path('logout/', views.hanlogout, name='hanlogout'),
]
