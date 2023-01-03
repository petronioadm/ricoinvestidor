from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def ativo (request):
    return HttpResponse('Estou em ativo')