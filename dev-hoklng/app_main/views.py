from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('처음으로 연결한 app')