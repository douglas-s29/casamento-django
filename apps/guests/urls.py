from django.urls import path
from . import views

app_name = 'guests'

urlpatterns = [
    path('convite/<uuid:token>/', views.convite, name='convite'),
]
