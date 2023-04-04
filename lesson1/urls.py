from django.urls import path
from lesson1 import views

urlpatterns = [
    path('', views.index, name='index'),
]
