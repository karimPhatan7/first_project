from django.shortcuts import render
from django.http import *

def karim(request):
    return HttpResponse('<h1><marquee>Hai Karim How are you</h1></marquee>')
def phatan(request):
    return HttpResponse('<h1 style=bg-color:"yellow"><marquee>Iam good What about you</h1></marquee>')

def nabi(request):
    return render(request,'nabi.html')
