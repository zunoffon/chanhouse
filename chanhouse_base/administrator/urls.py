from django.urls import path
from . import views

#  Namespacing URL names
app_name = 'administrator'

urlpatterns = [
    path('', views.index, name='index'),
]
