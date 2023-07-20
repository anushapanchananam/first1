from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def anusha(request):
    return HttpResponse('<marquee><h1>When i will get job god</h1></marquee>')

def vyshnavi(request):
    return HttpResponse('<h1>Everything will be fine</h1>')