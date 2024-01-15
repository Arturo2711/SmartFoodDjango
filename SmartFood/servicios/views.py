from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'servicios/index.html')

def services(request):
    return render(request, 'servicios/services.html')

def about(request):
    return render(request, 'servicios/about.html')

def contact(request):
    return render(request, 'servicios/contact.html')
