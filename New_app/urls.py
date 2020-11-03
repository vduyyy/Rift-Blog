from django.urls import path 
from . import views

urlpatterns = [
    path('TheRift', views.index), 
    path('register',views.register),
    path('login',views.login),
    path('logout', views.logout),
    path('league', views.league),
    path('top', views.top),
    path('mid', views.mid),
    path('jungle', views.jungle),
    path('adc', views.adc),
    path('support', views.support),
    path('go_back', views.go_back),
    path('builder', views.builder),
    path('path_build', views.path_build),
    path('log_out', views.logout),
    path('comment' ,views.comment)
]