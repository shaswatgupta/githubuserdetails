from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request) :
    return HttpResponse('Hello World!')

def secondView(request):
    return HttpResponse('My second View!')

