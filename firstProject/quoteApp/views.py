from django.shortcuts import render
from django.http import HttpResponse

def displayQuote(request):
    return HttpResponse("My name is AMG")

# Create your views here.
