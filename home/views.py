from django.shortcuts import render, redirect
from django.contrib.auth import logout

def calcular(v1, v2):
    return v1 + v2

# TODO: Teste de todo
def home(request):
    return render(request, 'home.html')

# FIXME: Teste de fixme
def my_logout(request):
    logout(request)
    return redirect('home')
