from django.shortcuts import render, HttpResponse
import requests
import json

# Create your views here.

def index(request) :
    return HttpResponse('Hello World!')

def secondView(request):
    return HttpResponse('My second View!')

def profile(request):
    req = requests.get('https://api.github.com/users/shaswatgupta')
    content = req.text
    return HttpResponse(content)

