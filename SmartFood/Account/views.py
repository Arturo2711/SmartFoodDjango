from django.shortcuts import render,redirect
from django.shortcuts import render
from . import forms
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import UserRegistrationForm
# Create your views here.
# Just remember, a view is essentially for return a HTTP response


def user_login(request):
    if request.method == 'POST':  # Se espera que la forma sea enviada via POST request
        # Se crea una instancia de la clase Login form and it's poulate by data from the request
        form = forms.LoginForm(request.POST)
        if form.is_valid():  # Validaciones necesairas y adicionales
            cd = form.cleaned_data
            # Autenticamos el usuario en los usuarios en la base de datos
            user = authenticate(request,
                                username=cd['Nombre'],
                                password=cd['Contrasena'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('recetario')
                else:
                    return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid login')
    else:
        form = forms.LoginForm()
    return render(request, 'account/login.html', {'form': form})


def register_done(request):
    return render(request, 'account/register_done.html')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request,
                          'account/register_done.html')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})

