from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def dhoni(request):
    return HttpResponse('<h1>MS.Dhoni Best Finisher From India</h1>') 
def raji(request):
    return HttpResponse('<h2>Raji Is My Best Friend</h2>')