from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),   # go to the hompage function in views.py
    path('count', views.count, name='count'),
    path('about', views.about, name='about'),
    ]
