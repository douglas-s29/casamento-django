"""
URL Configuration for wedding project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    
    # Public pages
    path('', include('apps.core.urls')),
    
    # Guests (RSVP)
    path('confirmacao/', include('apps.guests.urls')),
    
    # Gifts
    path('presentes/', include('apps.gifts.urls')),
    
    # Payments
    path('pagamento/', include('apps.payments.urls')),
    
    # Dashboard
    path('painel/', include('apps.dashboard.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
