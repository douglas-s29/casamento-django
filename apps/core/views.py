from django.shortcuts import render

def home(request):
    """Home page with hero section, countdown, and story"""
    return render(request, 'public/home.html')

def location(request):
    """Location page with map and directions"""
    return render(request, 'public/location.html')
