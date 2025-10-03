from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def homePage(request):
    return render(request, "biblioteca/homePage.html")


def profile(request):
    return render(request, "registration/profile.html")

def registro(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            user = formulario.save()
            login(request, user)
            return redirect('review-list')  
    else:
        formulario = UserCreationForm()
    
    context = {'form': formulario}
    return render(request, 'registration/registro.html', context)
