from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world from Django Docs!!!")

# Create your views here.
