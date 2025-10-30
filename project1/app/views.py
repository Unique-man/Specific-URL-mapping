from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def Home(request):
    return HttpResponse("welcome to home page")

def about(request):
    return HttpResponse("About page")