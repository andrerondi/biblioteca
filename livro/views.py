from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuario.models import Usuarios

# Create your views here.

def home(request):
    if request.session.get('usuario'):
        usuario = Usuarios.objects.get(id = request.session['usuario']).nome 
        return HttpResponse(f'Olá {usuario}')
    else:
        return redirect('/auth/login/?status=2')
