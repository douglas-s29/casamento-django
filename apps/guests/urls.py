from django.urls import path
from . import views

app_name = 'guests'

urlpatterns = [
    path('<uuid:uuid>/', views.rsvp, name='rsvp'),
]
