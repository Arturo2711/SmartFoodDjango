from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name="login"),
    path('registerDone/', views.register_done, name='register_done'),
    path('register/', views.register, name='register')
]