# All path specific to catcollector
from django.urls import path
from . import views

urlpatterns = [
    # Step 1: Define a path
    path('', views.home, name='home'),
    path('about/', views.about, name='about')
]