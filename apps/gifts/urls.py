from django.urls import path
from . import views

app_name = 'gifts'

urlpatterns = [
    path('', views.gift_list, name='list'),
]
