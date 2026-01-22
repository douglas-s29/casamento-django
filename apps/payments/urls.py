from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('criar/<int:gift_id>/', views.create_payment, name='create'),
    path('confirmacao/<int:payment_id>/', views.payment_confirmation, name='confirmation'),
    path('webhook/asaas/', views.asaas_webhook, name='webhook'),
]
