from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def virat(request):
    return HttpResponse('<h1>Virat Best Batsman in World<h1>')
def kavi(request):
    return HttpResponse('<h2>Kavi is Very Brave Girl</h2>')
