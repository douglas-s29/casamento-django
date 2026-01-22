from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('processar/<int:gift_id>/', views.process_payment, name='process'),
    path('sucesso/<int:payment_id>/', views.success, name='success'),
    path('webhook/', views.webhook, name='webhook'),
]
