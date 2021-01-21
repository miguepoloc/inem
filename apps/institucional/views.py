from django.shortcuts import render
from django.http import HttpResponse


def institucional(request):
    return render(request, 'institucional/institucional.html')
