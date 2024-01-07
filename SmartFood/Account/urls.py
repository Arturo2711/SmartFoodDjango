from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name="login"),
<<<<<<< HEAD
    path('registerDone/', views.register_done, name='register_done'),
=======
    path('registerDone',views.register_done,name='register_done'),
>>>>>>> origin/front_food
    path('register/', views.register, name='register')
]
