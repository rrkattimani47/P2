from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("HI WELCOME TO RASHMI'S PROJECT 2")#HttpResponse(HTML tag as an argument)

def home(request):
    return HttpResponse("<h1>Welcome to homepage<h1>")

def demo2(request):
        return render(request,"demo2.html")
