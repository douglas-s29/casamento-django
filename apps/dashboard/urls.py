from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='dashboard/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='home'),
    path('convidados/', views.guests_list, name='guests'),
    path('presentes/', views.gifts_list, name='gifts'),
    path('pagamentos/', views.payments_list, name='payments'),
    path('configuracoes/', views.settings, name='settings'),
]
