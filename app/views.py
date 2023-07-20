from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def ramesh(request):
    return HttpResponse('i am there with you')

def sailaja(request):
    return HttpResponse('<marquee><i><h1>we are with you<h1><i><marquee>')
