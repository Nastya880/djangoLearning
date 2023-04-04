from django.urls import path
from lesson2 import views

urlpatterns = [
    path('', views.index, name='index'),
    path('article/2003/', views.special_case_2003),
    path('article/<int:year>/', views.year_archive),

    #path('index/', views.index, name='index-view'),
    #path('bio/<username>/', views.bio, name='bio'),
]
