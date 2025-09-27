from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def homePage(request):
    return render(request, "biblioteca/homePage.html")


def profile(request):
    return render(request, "registration/profile.html")


def homeSec(request):
    return render(request, "registration/homeSec.html")


def registro(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('sec-home')

    else:
        formulario = UserCreationForm()
    context = {'form': formulario, }
    return render(request, 'registration/registro.html', context)
