from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.


def about(request):
    return HttpRequest("Code by Himself65")