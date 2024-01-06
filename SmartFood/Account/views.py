from django.shortcuts import render
from django.shortcuts import render
from . import forms
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from . import forms
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
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'account/logged_in.html')
                else:
                    return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid login')
    else:
        form = forms.LoginForm()
    return render(request, 'account/login.html', {'form': form})


def register_done(request):
    return render(request, 'account/register_done.html')

