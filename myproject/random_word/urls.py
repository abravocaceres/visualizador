from random import random
from django.urls import path
from . import views

#localhost:8000/random_word

urlpatterns = [
    path('', views.random_word),
    path('reset/', views.restart_counter)

]