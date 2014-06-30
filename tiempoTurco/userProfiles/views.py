from django.shortcuts import render
from django.contrib.auth import login, logout

from .forms import UserCreationEmailForm, EmailAuthenticationForm

# Create your views here.
def signUp(request):
    form = UserCreationEmailForm(request.POST or None)

    if form.is_valid():
        form.save()

        #Ingresar
        #Crear Perfil de Usuario
        #Redireccionar al Home

    return render(request, 'registerUser.html', {'form': form})

def loginUser(request):
    form = EmailAuthenticationForm(request.POST or None)

    if form.is_valid():
        #Ingresar usuario
        login(request, form.get_user())
        #Redirrecionamos al Home


    return render(request, 'loginUser.html', {'form':form})