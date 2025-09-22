from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def homeSec(request):
    return render(request, "seguranca/homeSec.html")


def registro(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('sec-home')

    else:
        formulario = UserCreationForm()
    context = {'form': formulario, }
    return render(request, 'seguranca/registro.html', context)
