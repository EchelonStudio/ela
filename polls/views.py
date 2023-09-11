from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('We are hitting our first pythin method')


def create(request):
    return HttpResponse('Create new polls page')


def store(request):
    return HttpResponse('Store new polls')