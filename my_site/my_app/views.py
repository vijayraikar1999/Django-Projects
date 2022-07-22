from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(requests):
    return HttpResponse('Hello! This is a view inside my app.')
