from django.urls import path
from .views import index, services, about, contact

urlpatterns = [
    path('index/', index, name='index'),
    path('services/', services, name='services'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]

