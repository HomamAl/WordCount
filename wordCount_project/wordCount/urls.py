
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='index'),
    path('count/', views.count, name='count'),
    path('aboutme/', views.aboutme, name='aboutme'),
]
