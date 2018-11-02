from django.shortcuts import render, redirect
from django.contrib.auth import logout

# TODO: Teste de todo
def home(request):
    a = 1
    b  = 2
    c = a + b
    return render(request, 'home.html', {'c':c})

# FIXME: Teste de fixme
def my_logout(request):
    logout(request)
    return redirect('home')
