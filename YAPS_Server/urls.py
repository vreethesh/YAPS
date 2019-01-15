from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ser', views.search, name='search'),
    path('p', views.passReg, name='passngr'),
    path('c', views.carReg, name='car'),
]